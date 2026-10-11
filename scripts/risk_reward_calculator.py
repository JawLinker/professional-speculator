"""Math only. No prices fetched, trend inferred, verdict or position issued."""
from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import json
import math
from pathlib import Path
import sys

DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / "references" / "defaults.json"


def number(value, label, *, positive=False):
    if isinstance(value, bool):
        raise ValueError(f"{label} must be a finite number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError(f"{label} must be a finite number") from None
    if not result.is_finite() or (positive and result <= 0):
        raise ValueError(f"{label} must be finite" + (" and positive" if positive else ""))
    return result


def load_config(path=DEFAULT_CONFIG):
    with Path(path).open(encoding="utf-8") as stream:
        data = json.load(stream)
    try:
        rr = data["rr"]
        bounds = [number(x, "rating bound", positive=True) for x in rr["rating_upper_bounds"]]
        labels = rr["ratings"]
        if len(bounds) != 4 or any(a >= b for a, b in zip(bounds, bounds[1:])):
            raise ValueError("four strictly increasing positive rating bounds required")
        if not isinstance(labels, list) or len(labels) != 5 or any(not isinstance(x, str) or not x.strip() for x in labels):
            raise ValueError("five nonempty rating labels required")
        cost = number(rr.get("cost_per_unit_default", 0), "default cost")
        if cost < 0:
            raise ValueError("default cost cannot be negative")
    except (KeyError, TypeError) as exc:
        raise ValueError("config requires rr.rating_upper_bounds and rr.ratings") from exc
    return bounds, labels, cost


def rating(rr, bounds, labels):
    # First three boundaries are exclusive; the final upper boundary inclusive.
    for index, bound in enumerate(bounds):
        if rr < bound or (index == len(bounds) - 1 and rr == bound):
            return labels[index]
    return labels[-1]


def json_number(value):
    result = float(value)
    if not math.isfinite(result):
        raise ValueError("calculation exceeds supported JSON numeric range")
    return result


def calculate(entry, stop, targets, *, direction="long", cost_per_unit=None, config=DEFAULT_CONFIG):
    bounds, labels, default_cost = load_config(config)
    e = number(entry, "entry", positive=True)
    s = number(stop, "stop", positive=True)
    cost = default_cost if cost_per_unit is None else number(cost_per_unit, "cost_per_unit")
    if cost < 0:
        raise ValueError("cost_per_unit cannot be negative")
    if direction not in ("long", "short"):
        raise ValueError("direction must be long or short")
    if not isinstance(targets, (list, tuple)) or not targets:
        raise ValueError("at least one target required")
    sign = Decimal(1) if direction == "long" else Decimal(-1)
    risk = sign * (e - s)
    if risk <= 0:
        raise ValueError("long stop must be below entry; short stop must be above entry")
    net_risk = risk + cost
    rows = []
    for target in targets:
        t = number(target, "target", positive=True)
        reward = sign * (t - e)
        if reward <= 0:
            raise ValueError("long targets must be above entry; short targets must be below entry")
        net_reward = reward - cost
        gross_rr = reward / risk
        net_rr = net_reward / net_risk
        rows.append({
            "target": json_number(t),
            "gross_reward_per_unit": json_number(reward),
            "gross_reward_pct": json_number(reward / e * 100),
            "gross_rr": json_number(gross_rr),
            "gross_rating": rating(gross_rr, bounds, labels),
            "net_reward_per_unit": json_number(net_reward),
            "net_reward_pct": json_number(net_reward / e * 100),
            "net_rr": json_number(net_rr),
            "net_rating": rating(net_rr, bounds, labels),
            "binary_break_even_probability": json_number(net_risk / (net_risk + net_reward)) if net_reward > 0 else None,
        })
    return {
        "calculation_only": True,
        "direction": direction,
        "entry": json_number(e), "stop": json_number(s),
        "cost_per_unit": json_number(cost),
        "cost_basis": "provided_or_configured_cost_assumption" if cost else "zero_cost_gross_basis",
        "gross_risk_per_unit": json_number(risk), "gross_risk_pct": json_number(risk / e * 100),
        "net_risk_per_unit": json_number(net_risk), "net_risk_pct": json_number(net_risk / e * 100),
        "targets": rows,
        "limitations": "No market validation. Stop execution and loss cap are not guaranteed. Break-even probability is arithmetic, not a win-rate estimate.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--entry", required=True)
    parser.add_argument("--stop", required=True)
    parser.add_argument("--target", action="append", required=True)
    parser.add_argument("--direction", choices=("long", "short"), default="long")
    parser.add_argument("--cost-per-unit")
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    args = parser.parse_args(argv)
    try:
        result = calculate(args.entry, args.stop, args.target, direction=args.direction,
                           cost_per_unit=args.cost_per_unit, config=args.config)
    except (ValueError, OSError, InvalidOperation, OverflowError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, allow_nan=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
