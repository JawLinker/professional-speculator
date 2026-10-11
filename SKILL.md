---
name: professional-speculator
description: "判断股票、ETF、指数等公开证券现在是否值得交易，检查趋势、1-2-3/2B反转、入场位置、失效位、风险收益和纪律，给出买/等/卖的条件化计划。用于现在能不能买、好买点、趋势反转、交易赔率、入场退出及按照专业投机原理分析；纯商业模式、长期基本面和估值建模交给 Public Equity Investing。"
---

# 专业投机决策系统 · Professional Speculator

负责 **Is this a good trade right now?**，分别回答好公司、好资产、好交易。Investment Thesis 与 Trade Setup 不互相替代。借鉴 Victor Sperandeo 的价格结构与纪律，实施阈值为可调整约定，非书籍摘要、预测器或下单工具。

## 启动与依赖

1. 识别证券、交易所、币种、截至时间、方向、周期、持仓状态。多地上市存在实质歧义才询问。周期缺省：按 defaults.json（初始周线主趋势、日线结构）明确数周至数月候选；持仓未知只分析候选，不能暗示已有持仓。
2. 读取 [decision-policy.md](references/decision-policy.md)、[defaults.json](references/defaults.json)、[output-contract.md](references/output-contract.md)。完整分析读取 [trend-framework.md](references/trend-framework.md)；局部反转问题只展开相关参考，不强求完整报告。
3. 实时事实使用实际可用工具/公开来源，按 [data-and-markets.md](references/data-and-markets.md) 记录时点、复权、覆盖和缺失。单报价不能推导波段或反转。用户数据标注 `Analysis based on provided data`；行情不可得标注 `Market data unavailable`。未知不是 No/Neutral。
4. 基本面、组合风险、宏观、监控读 [handoff.md](references/handoff.md)，再读实际安装的 Public Equity Investing 路由器和所选子 Skill。交接是阅读并执行支持流程，不存在假定的 call_skill API；本 Skill 保留交易裁决责任。

本 Skill 的相对路径以本 SKILL.md 所在目录解析；运行脚本用解析后的绝对路径或将工作目录设为 Skill 根，不能从用户项目目录猜 scripts/。配置覆盖和值来源在决策卡说明。

## 决策依赖链

按顺序建立证据。遇否决立即限制候选评级，后续好消息不能把失败候选翻为 BUY；仍可解释和管理已有持仓。

| 阶段 | 必须解决 | 下游依赖 |
| --- | --- | --- |
| 市场 → 行业 → 证券 | 主/次趋势、risk-on/off、波动；方向与信心分开 | 选择趋势追随或独立逆势候选 |
| 价格结构 | 有时间价格的 HH/HL/LH/LL、趋势线锚点、支撑阻力 | 趋势是否有效 |
| 反转 | 1-2-3 顺序证据、2B 穿越/收回证据 | 追随、等待或退出 |
| 位置 | 入场区、近端障碍、支撑/失效距离、追价风险 | Entry 与结构失效 |
| 失效 → 赔率 | Trade invalidation、止损方式、目标依据、成本 | RR 门槛 |
| 宏观/基本面 | 确认/背离、催化剂、独立 Thesis invalidation | 信心与事件风险 |
| 风险预算 | 组合风险、流动性、跳空/制度、最紧约束 | 规模框架与可执行性 |
| 心理纪律 | 仅依据明确陈述判断偏差 | 是否暂停新增风险 |
| 裁决/监控 | gates → 评分上限 → 状态 → IF/AND/THEN | 观察、证伪与退出规则 |

### 结构与反转

Price Structure > Trend > Support/Resistance > Invalidation > RR > Macro > Fundamentals > Indicators；指标只辅助。

读 [123-reversal.md](references/123-reversal.md) 判断同一周期、同一事件顺序完成的 0/3–3/3。无证据用 Unknown，不伪造0/3；2/3 只能 weakening，不能 confirmed reversal。读 [2b-reversal.md](references/2b-reversal.md) 核验前高/低、穿越、窗口内收回、确认；2B 不是完整主趋势反转的同义词。

确认反转与候选方向冲突先否决该候选；反向交易必须建立自己的新结构、失效位和赔率，不能沿用已经失败的趋势追随 setup。

### 失效位、赔率与确认

读 [risk-reward.md](references/risk-reward.md)。先锁定结构失效再算赔率，不能收紧到无结构意义的止损或挑远端目标美化 RR。每个目标有依据、周期和到达前障碍；第一可执行目标或明确分批计划决定门槛。运行 `python scripts/risk_reward_calculator.py --entry 31.20 --stop 29.80 --target 34 --target 35.80` 复算；Short 用 `--direction short`。脚本仅计算，不识别趋势或裁决。

宏观考虑经济周期、货币/财政、利率、信用、通胀、汇率、流动性、产业/监管；商品、广度、资金流按相关性与可得性检查。Macro/Policy/Liquidity 分别 Positive/Neutral/Negative/Unknown；综合 Strong/Moderate/Weak/Contradictory/Unknown，并说明机制。背离降低信心或改变规则，不机械否决。

基本面返回 Alignment、驱动/风险、催化剂、Thesis invalidation；Alignment 用 Strong Positive/Positive/Neutral/Negative/Strong Negative/Unknown。ETF/指数按篮子、行业/因子、指数制度与追踪风险确认，不虚构公司财报。好基本面不能覆盖坏位置、坏赔率或缺失效位。

组合风险优先交给 portfolio-risk-management；账户未知只给条件框架。Stop 不保证亏损封顶，Short 区分绝对损失上限与情景预算。中国证券读 [a-share-notes.md](references/a-share-notes.md)。读 [psychology-checklist.md](references/psychology-checklist.md)：心理信息不足输出 `Not enough information`，不默认 Low；明确 extreme FOMO/revenge trading 暂停新增风险，不因此自动卖出旧仓。

## 裁决与终检

严格执行 decision-policy 优先级。数据不足不能造价格，已知失效不能被缺失数据遮蔽；候选与旧仓分别裁决，候选 RR<1 不自动要求卖旧仓。

- 多头候选：STRONG BUY SETUP / BUY SETUP / WAIT / WATCH / AVOID / PASS。
- 空头候选：STRONG SHORT SETUP / SHORT SETUP 等对称标签；明确借券、交易许可、挤空风险，不标 BUY。
- 已持仓：HOLD / ADD ONLY IF / REDUCE / EXIT；另列新增风险是否过关。
- 严重数据缺失：WATCH + Data Status INSUFFICIENT DATA，无法评级则 Unrated。

SETUP 是通过研究门槛的条件候选，触发待定不等于立即买入；执行风险、预算、触发与禁止追价规则须明确。A+/A/A-/B+/B/B-/C/D 按 defaults 权重、证据覆盖和 cap 计算；未知不补中性分，高分不是概率，veto 优先。

完整结论至少展示一个“证据 → gate → 裁决”路径并交付紧凑决策卡，字段与条件规则见 output-contract。局部问题只答相关判断、交易影响和缺口。未经用户要求不启用定时监控、改组合记录或执行交易。

## 验证

[behavioral-cases.md](references/behavioral-cases.md) 提供十例与边界，人工/独立模型验证使用，不能充当真实行情。数学回归：`python -m unittest discover -s tests -v`。数学回归不证明所有未来模型调用都遵守 Skill；保留失败案例并依实际观察修复。
