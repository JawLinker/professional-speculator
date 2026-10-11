import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from risk_reward_calculator import calculate, DEFAULT_CONFIG


class RiskRewardTests(unittest.TestCase):
    def test_requested_example_all_targets(self):
        result = calculate("31.20", "29.80", ["34", "35.80"])
        self.assertAlmostEqual(result["gross_risk_pct"], 4.487179487)
        self.assertEqual(result["targets"][0]["gross_rr"], 2)
        self.assertAlmostEqual(result["targets"][1]["gross_rr"], 3.285714286)
        self.assertEqual([x["gross_rating"] for x in result["targets"]], ["Good", "Excellent"])

    def test_long_short_symmetry(self):
        long = calculate(100, 95, [110])["targets"][0]
        short = calculate(100, 105, [90], direction="short")["targets"][0]
        self.assertEqual(long["gross_rr"], short["gross_rr"])
        self.assertEqual(long["gross_reward_pct"], short["gross_reward_pct"])

    def test_costs_can_fail_previously_good_rr(self):
        result = calculate(100, 95, [105], cost_per_unit=1)
        self.assertAlmostEqual(result["targets"][0]["net_rr"], 4 / 6)
        self.assertEqual(result["targets"][0]["net_rating"], "Very Poor")

    def test_negative_net_reward_is_reported(self):
        row = calculate(100, 95, [101], cost_per_unit=2)["targets"][0]
        self.assertLess(row["net_rr"], 0)
        self.assertIsNone(row["binary_break_even_probability"])

    def test_exact_rating_boundaries(self):
        for target, label in [(100.99, "Very Poor"), (101, "Poor"), (101.5, "Acceptable"), (102, "Good"), (103, "Good"), (103.01, "Excellent")]:
            with self.subTest(target=target):
                self.assertEqual(calculate(100, 99, [target])["targets"][0]["gross_rating"], label)

    def test_invalid_numbers_and_geometry(self):
        calls = [
            (0, 95, [110], {}), (100, 100, [110], {}), (100, 105, [110], {}),
            (100, 95, [90], {}), (100, 95, [], {}),
            (100, 95, [90], {"direction": "short"}),
            (100, 105, [110], {"direction": "short"}),
            ("NaN", 95, [110], {}), (100, "Infinity", [110], {}),
            (100, 95, ["-Infinity"], {}), (100, 95, [110], {"cost_per_unit": -1}),
            (True, 95, [110], {}), (100, 95, [110], {"cost_per_unit": "NaN"}),
        ]
        for e, s, ts, options in calls:
            with self.subTest(entry=e, stop=s, targets=ts, options=options):
                with self.assertRaises(ValueError):
                    calculate(e, s, ts, **options)

    def test_config_override(self):
        config = json.loads(DEFAULT_CONFIG.read_text(encoding="utf-8"))
        config["rr"]["rating_upper_bounds"] = [1, 2, 3, 4]
        config["rr"]["cost_per_unit_default"] = 0.5
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "config.json"
            path.write_text(json.dumps(config), encoding="utf-8")
            result = calculate(100, 95, [110], config=path)
        self.assertEqual(result["targets"][0]["gross_rating"], "Acceptable")
        self.assertEqual(result["cost_per_unit"], 0.5)

    def test_invalid_config_fails(self):
        for bounds in [[1, 1, 2, 3], [1, 2], [0, 1, 2, 3], [1, 2, 3, "Infinity"]]:
            with self.subTest(bounds=bounds), tempfile.TemporaryDirectory() as temporary:
                config = json.loads(DEFAULT_CONFIG.read_text(encoding="utf-8"))
                config["rr"]["rating_upper_bounds"] = bounds
                path = Path(temporary) / "bad.json"
                path.write_text(json.dumps(config), encoding="utf-8")
                with self.assertRaises(ValueError):
                    calculate(100, 95, [110], config=path)

    def test_entry_zone_worst_end_and_near_target(self):
        low = calculate(100, 95, [110, 125])["targets"]
        high = calculate(104, 95, [110, 125])["targets"]
        self.assertLess(high[0]["gross_rr"], low[0]["gross_rr"])
        self.assertLess(high[0]["gross_rr"], 1)
        self.assertGreater(high[1]["gross_rr"], 2)

    def test_binary_break_even_is_only_arithmetic(self):
        row = calculate(100, 95, [110])["targets"][0]
        self.assertAlmostEqual(row["binary_break_even_probability"], 1 / 3)

    def test_cli_output_and_error_exit(self):
        script = str(ROOT / "scripts" / "risk_reward_calculator.py")
        success = subprocess.run([sys.executable, script, "--entry", "100", "--stop", "105", "--target", "90", "--direction", "short"], capture_output=True, text=True)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(json.loads(success.stdout)["targets"][0]["gross_rr"], 2)
        failure = subprocess.run([sys.executable, script, "--entry", "100", "--stop", "100", "--target", "110"], capture_output=True, text=True)
        self.assertEqual(failure.returncode, 2)
        self.assertEqual(failure.stdout, "")
        self.assertIn("ERROR", failure.stderr)


if __name__ == "__main__":
    unittest.main()
