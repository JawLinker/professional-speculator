# 先 gate，再评分，再状态

门槛从 defaults.json 读取；用户明确覆盖时报告调整项/原因。这些是操作约定，不是作者原书参数或胜率。

## 证据与持仓

维护 ledger：`id | evidence/source/time | Pass/Fail/Unknown/Not applicable | effect | resolution`。Unknown 不等于通过。分别记录 company thesis、asset attractiveness、trade setup、existing-position action。账户缺失不阻塞候选研究，但不能给具体仓位数量。

更新/合并资料时，将新材料与旧材料的证券、周期、时点和规则版本对齐。用户明确的修订或同一时点更具体的原始事件证据可替代对应旧概述，保留替代记录；新的事件可使旧风险screen失效。不能仅因更新了Entry就暗改旧No-chase/stop规则。无法解决的身份、时点、价格冲突→G0，未解前不用混合价格算可执行RR；已有确定失败仍单列。用户已提供充分事实/风险支持包时可以条件使用并标来源，未实际执行的新handoff不能声称已完成。

持仓方向已知且已验证失效规则触发 → EXIT 风险管理姿态；不能因好基本面改 HOLD。停牌/封板等要写“退出条件已触发，成交受限”，不承诺失效价成交。资料不足且无可靠失效证据 → 持仓行动待复核，不编 HOLD/EXIT。成本不是结构失效依据。

## 新开仓/加仓 gate

所有 gate 都检查，报告并列阻碍。

| ID | 条件 | 默认效果 |
| --- | --- | --- |
| G0 | 身份、行情时点、周期价格结构等关键证据不足/冲突/陈旧 | WATCH + INSUFFICIENT DATA；Unrated 或最多 C，不造 RR |
| G1 | 有足够结构数据却找不到合理 Trade invalidation；或完全依赖希望 | PASS，最多 C |
| G2 | stop 与方向几何错误、目标无依据/不合理 | PASS 当前方案，需重建；最多C，无法计算则Unrated |
| G3 | 成本后第一可执行目标 RR < new_setup_veto_below | PASS，最多 C；未来更好价格可另列 WAIT 计划，当前仍 PASS |
| G4 | 方向与已确认结构反转冲突 | AVOID 当前方向，D；旧仓检查失效，不自动反向开仓 |
| G5 | 方向冲突/结构 under pressure 但未确认反转 | WAIT；2/3 不能称 confirmed |
| G6 | 确认流动性不足、不可借券/方向不允许、最小单位超预算、结构止损太远且无法控制风险 | PASS/AVOID，当前表达最多C，不用无意义窄止损解决 |
| G7 | 临近重大事件且跳空风险不可估算；制度/价格限制阻塞合理入场 | WAIT，量化纳入预算才可重评 |
| G8 | 位置 Poor/Very Poor、超出入场区、RR 低于 setup 门槛、触发没定义 | WAIT，最多 B，禁止追价 |
| G9 | 明确 revenge trading / extreme FOMO | WAIT 新风险 + 有证据的 Risk Warning，不自动卖旧仓 |
| G10 | 缺宏观/财务确认；执行所需借券、流动性、事件/交易制度未知 | 确认缺失最多 B+；执行未知 WAIT/WATCH，不能称 setup 已通过 |

优先级：明确旧仓失效优先；新候选确认方向反转 AVOID → 其他确定硬失败 PASS → 临时阻碍 WAIT → 只有缺数据/未建方案 WATCH。可同时报告 INSUFFICIENT DATA 与确定失败，G0 不遮蔽已知 G1/G3/G4。没有行情而无法查失效位是 Unknown→WATCH；有行情却找不到失效位是 Fail→PASS。

“止损太远导致不可控”须有预算/最小单位/跳空/流动性证据，不能只凭百分比大。心理未知不属于执行硬门槛。Macro Contradictory/Fundamental Negative 要解释并降低信心；独立核心证伪或风险 gate 成立才否决。

G4要求独立的已确认方向结构反转；**confirmed 2B本身只触发G5警告/重审，不直接等于G4**。有其他证据确认反转才用G4。Short情景预算可通过条件研究；用户明确绝对亏损上限却无已定价限定损失保护→G6拒绝该表达。预算解释未知且决定执行可行性→G10待确认，不能宣称绝对封顶。

## 评分与 cap

模块0–100，逐项一行证据：90–100强支持、70–89支持有限制、50–69混合、25–49弱/冲突、0–24失效。RR五档参考分10/35/60/80/95。位置和趋势不能只按涨幅评分。

`known_contribution=Σ(weight×score/100)`；Coverage=已知权重；区间 `[known_contribution, known_contribution+missing_weight]`。不重新归一化已知部分，不给未知补50分。区间下界转换为 defaults 等级，再取所有 cap 中最严格者；关键数据严重缺失直接 Unrated。分数不是胜率。

重要确认缺失按 missing_confirmation_grade_cap（初始B+）；心理未知按 unassessed_psychology_grade_cap（初始A-）；关键缺失按 missing_core_grade_cap（初始C，严重不足仍Unrated）。2/3反转、坏位置、临时阻碍最多B；G1/G2/G3/G6最多C（无法计算则Unrated）；反转冲突D。好公司不解禁任何 veto。

评分有分析判断空间，行为验收不要求C01必定Strong或唯一数值。Strong需展示逐模块证据充分、达到门槛的计算；对是否达到Strong存在未解的实质疑虑时采用普通SETUP。不能为达到预期标签反向调分。

## 状态与激活

所有新风险 gate 通过、RR 达 setup 门槛、质量≥setup_minimum（初始B+）、方向/位置/失效/目标/风险清楚 → BUY SETUP（空头对称）。≥strong_setup_minimum（初始A）且关键证据充分、趋势位置强、事件和纪律无实质疑虑 → STRONG BUY SETUP。分数够但 gate 不过仍 WAIT/PASS；宏观相反不机械禁止，若仍通过须解释。

WATCH=补证据/建方案；WAIT=已有方案等价格/时序/事件/风险条件；PASS=拒绝当前方案；AVOID=方向/表达不宜；HOLD=旧仓逻辑有效；ADD ONLY IF=新增风险也通过并有预算；REDUCE=预算/集中度/事件约束；EXIT=失效/硬预算约束。无持仓不使用旧仓动作。

Quality、Trend Confidence、Analysis Confidence、Execution Readiness、Trigger Status 分列。触发未到可以 BUY SETUP/Trigger Pending，不能称已激活。触发后按实际入场重算RR、验证可成交/预算；过度上涨转 WAIT。新信号使旧setup退役/重审，不沿用旧评分。

终检须展示决定性 ledger 行，以及入场、作废、禁止追价、事件重审四类 IF/AND/THEN；研究规则不授权真实下单。
