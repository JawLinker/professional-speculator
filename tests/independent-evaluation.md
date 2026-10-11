# 独立 forward evaluation

评估日期：2026-10-11。仅阅读本 Skill、工作流程需要的 references、计算脚本和 `tests/forward_requests.json`；未读取 `behavioral-cases.md` 或父任务总结。未浏览、访问外部服务、执行交易、启用监控、读取账户配置或修改 Skill。所有证券与事实都是合成输入。

## 评估方法与共同前提

- `changes` 覆盖 common_packet；`replace_packet` 整包替换。`structure_event`、`event`、`stored_rule` 的具体证据优先于冲突的基线概述。没有覆盖的基线继续适用。
- Data Status 为 `Analysis based on provided data / Synthetic`。provided/verified 表述按测试事实包接受，未假称独立核实了真实市场。基线风险 screen 是用户提供的条件研究输入；我没有执行 Public Equity Investing handoff，不能称“风险 owner 已被调用”。没有账户数量不否定研究候选，但不给具体数量或实盘 readiness。
- 基线：市场/行业周线高低点上升，Risk-On，Normal volatility，Trend Confidence High；证券日线低点90→95、高点100→105，HH/HL。预选上涨线85（07-10）→95（09-10）保持有效。价格100，入场99.5–100，支撑97–98，结构失效95。基本面 Strong Positive；Macro/Policy/Liquidity 均 Positive，综合 Strong。产品里程碑在4周后，无基线财报 gap 不确定性。
- 基线1-2-3：第一项 No（包中明确完整后续数据无有效破线），后两项 Not applicable，0/3 / Not active。不能因为高低点上升就证明不存在所有2B；没有明确2B路径的例子保持 Unknown，而非捏造 None。这个非必要反转细节不自动构成 G0 核心不足。
- 基线心理：自述不追价、不追回亏损、遵守预算和失效且不受成本左右，支持当前 FOMO/Revenge/Anchoring/Sunk Cost 为 Low；Confirmation Bias、Overconfidence 没有独立证据，Unknown。整体风险暂评 Low，限于此次明确自述，不能当永久属性。
- 基线评分按权重顺序（趋势20/位置15/RR20/宏观10/基本面15/催化5/风险10/纪律5）采用95/95/80/95/95/90/90/90：贡献19/14.25/16/9.5/14.25/4.5/9/4.5，总91，Coverage100%，区间[91,91]，A。RR Good 对应80；其余分数是有证据的分析判断，不是唯一确定值。否决案例只报告决定性 cap，不把继承的A当最终评级。
- 所有 Pending setup 都须触发后按实际价格、成本、第一障碍及预算重算。研究条件成立不授权下单。没有真实执行通道，Execution Readiness 至多 Conditional，不宣称可立刻成交。

实际运行 bundled Python 调用了 Skill 的计算脚本，核验 C01/C02/C15/C16：

| 例 | Entry / Stop / Cost | 目标 | Gross RR | Net或零成本 RR | 评级 |
|---|---|---|---:|---:|---|
| C01 | 100 / 95 / 0.1 | 111 | 2.200000 | 2.137255 | Good |
| C01 | 同上 | 120 | 4.000000 | 3.901961 | Excellent |
| C02 | 100 / 90 / 0 | 108 | 0.800000 | 0.800000 | Very Poor |
| C15 short | 100 / 104 / 0.1 | 90 | 2.500000 | 2.414634 | Good |
| C16 | 104 / 95 / 0 | 110 | 0.666667 | 0.666667 | Very Poor |
| C16 | 同上 | 125 | 2.333333 | 2.333333 | Good |

零成本数据只是零成本假设下的赔率；不会称经过市场核实的实际净成本。二元盈亏平衡概率不作胜率使用。

## 逐例结果

### C01 — 全部基础门槛通过，等待触发

- **Verdict：STRONG BUY SETUP；Quality A（91）；Trigger Pending；Execution Conditional。** 公司好、资产趋势支持、交易位置与第一目标赔率通过是三个独立判断。
- 决定性 ledger：HH/HL与完整未破线证据→G4/G5 Pass；100≤入场上限100且第一净RR2.137255≥2→G3/G8 Pass；给定 gap/流动性/许可条件 screen→风险研究门槛 Pass；无事件及纪律阻碍。触发尚未到不等于 G8 Fail，触发已明确定义。
- 1-2-3：0/3 / Not active；2B Unknown（未给具体路径）。心理依共同前提。
- 最小规则：IF 支撑97–98回测守住 AND 一个已完成日线收盘收复100、实际价仍在99.5–100、成本后首目标RR≥2、风险/事件 screen仍有效 THEN SETUP ACTIVE；IF 盘中有效触及/跌破既定95退出阈值 THEN setup作废；IF >101或RR<2 THEN WAIT、不追；IF 里程碑/订单/政策事实改变 THEN 重审，不继承A。最近已完成日线及产品里程碑后复核。
- 缺口：具体账户数量未请求；无实际 handoff/真实执行校验。止损触及还是严格跌破的边界在基线没有定义，执行前须明确；不能由“95 stop”假造精准成交。

### C02 — 好公司不能覆盖赔率硬失败

- **Verdict：PASS 当前候选；Quality cap C。** 第一目标108的零成本RR0.8<1。
- ledger：已提供有效结构止损90且没有更紧合理止损→G1 Pass；几何90<100<108→G2 Pass；RR0.8→G3 Fail→PASS。风险10%本身没有证明不可控，不凭百分比另造G6。
- 1-2-3继承0/3；心理没有新的问题。不得把强基本面改成BUY，也不得缩到没有结构意义的止损。
- 最小规则：IF 仍采用Entry100/Stop90/Target108 THEN PASS；IF 新的真实入场及触发能建立 AND 首RR≥2、结构与预算仍成立 THEN 重建候选。零成本下理论Entry≤96满足RR≥2，但不能直接拿96当已确认买点；IF 已知止损失效 THEN 作废；IF 未定义新触发/追价界线 THEN WATCH/WAIT；事件变化重审。
- 缺口：新入场区/触发需重建。无旧仓，不输出EXIT。

### C03 — 同一日线事件完整3/3，旧仓规则触发

- **Verdict：旧多头 EXIT；新增多头 AVOID；旧方向setup Quality D。** 日线反转不自动宣称周线Bear。
- 1-2-3：①09-22 close96<预选线98 Yes；②之后09-24反弹高101<105，09-28已确认 Yes；③反应低94形成于09-23、处于破线后/失败反弹前，09-30在反弹确认后close92<94 Yes。3/3，日线 Confirmed reversal。
- ledger：3/3+stored exit rule→旧仓失效优先→EXIT；confirmed日线反转与long冲突→G4 Fail→AVOID/D。92也低于旧HL95；不拿失效后的95重新计算当前多头RR。
- 最小规则：IF 此同一事件3/3且stored exit规则成立 THEN 退出风险姿态；成交能力按现实复核，不承诺95成交；IF 欲做空 THEN 另建空头结构、借券、失效及目标；IF 要恢复多头 THEN 新事件/新结构重审，不能继承旧A。
- 心理没有新的偏差证据；不因有旧仓默认高风险。缺口：实际退出报价/流动性、仓位数量未给；不影响“规则已触发”的结论。

### C04 — 2/3，尚未确认反转

- **Verdict：未确认日线反转；long候选 WAIT；Quality cap B。**
- ①破线09-22 Yes；②失败反弹101于09-28确认 Yes；③最新96仍高于预选94 No/Pending。2/3，weakening/Possible reversal，不能说3/3。周线主趋势仍Bull。
- ledger：结构 under pressure、第三项未发生→G5 Fail→WAIT；当前96也不在99.5–100入场区→G8阻碍。
- 最小规则：IF 反弹确认之后有一个完成日线close<94 THEN 该日线事件3/3、long AVOID并复核旧仓规则；IF 趋势线夺回/新高使旧条件退役 AND 新结构、位置、首RR与风险重过 THEN 另建setup；IF >101 THEN 不沿用旧追价计划。事件改变重审。
- 心理依基线。缺口：2B独立路径Unknown；下一完整收盘决定第三项，不编造未来。

### C05 — 基本面强，交易结构仍在承压

- **Verdict：WAIT；Quality cap B。** Company Strong Positive，Trade暂不过门槛。
- 结构叙述给出破线、已确认失败反弹、未破94，支持2个已知条件与G5；但此例没有各步日期/明确确认先后，标“叙述支持2/3；时间证据未完整复现”，不把它当严谨3/3。周Bull、日Weak可以并存。
- ledger：daily under pressure→G5→WAIT；96<入场下端99.5→G8；基本面不能解除。
- 最小规则：IF 补足同一事件时间并在失败反弹确认后close<94 THEN日线反转/long AVOID；IF 结构修复且重新通过入场/首RR/风险 THEN 新候选；IF 原计划失效或价格>101 THEN 不追；催化/核心订单变化重审。
- 心理依基线。缺口：1-2-3时间 ledger、修复后新的触发/失效。不能因96使机械RR变高就宣布是买点。

### C06 — 足够数据但无可辩护失效位

- **Verdict：PASS；Quality cap C；RR unavailable。**
- ledger：“full price packet checked”、没有结构或量化失效、仅希望上涨→G1 Fail→PASS。不是单纯数据缺失，不能降格成WATCH并逃避失败。
- 1-2-3基线0/3；好趋势不替代Trade invalidation。提出方案只靠希望，不能据此诊断用户人格或自动把六类心理都评High。
- 最小规则：IF 仍无可验证结构/量化失效 THEN PASS；IF 新证据产生合理失效与同币种风险价 AND 首RR≥2、触发/预算/执行通过 THEN 重新研究；失效/禁止追价阈值未建立前不激活；重大事件改变重审。
- 缺口：有效失效位、可量化风险、据此重算赔率；不可把null stop补成95。

### C07 — 没行情，不能造结构或赔率

- **Verdict：WATCH + INSUFFICIENT DATA；Quality Unrated。**
- ledger：整包替换后没有报价/OHLC/波段/财务→G0 Unknown；失效位、目标、RR、趋势/宏观均Unknown；执行未知G10。1-2-3 Unknown（known satisfied 0，unknown 3），不是0/3；2B Unknown。心理 Not enough information。
- 最小规则：IF 取得用户提供的同周期价格/时点/证券身份及结构数据 THEN 重建ledger；IF 没有效失效与目标 THEN 不计算RR、不激活、不编追价阈值；有新事件资料后复核。受测试禁止外查约束，只等待所需输入。
- 缺口：交易所/币种/as_of/方向/周期/价格历史、基本面宏观、风险与心理。可采用Skill缺省周期作明确假设，但不能编市场时间。

### C08 — 原有失效已触发，成本不能改规则

- **Verdict：旧仓 EXIT；新增风险 WAIT/旧setup作废，不能用成本120继续HOLD。** 旧仓动作不是交易质量等级；旧setup Invalid，恢复新增候选最多B，待结构重建。
- ledger：verified可执行92<stored盘中退出阈值95且执行许可明确→旧仓失效优先→EXIT。其他完整反转证据未给，不凭一次现价推3/3；1-2-3的新事件完成度Unknown。
- 心理：明确“拒绝低于120卖出”“即使95失效已破也要回本”→Anchoring/Sunk Cost High；总体Emotion Risk High。未明确revenge/FOMO，不强贴该两项High；成本不构成支撑。
- 最小规则：IF verified执行价<95 AND规则是盘中退出且许可有效 THEN 执行退出风险姿态；IF 重新开仓 THEN 必须以现价/新结构/预算重写独立计划；IF 再以成本推翻失效 THEN 暂停新增；价格/事件变化复核。退出不承诺在95成交。
- 缺口：数量、实际成交结果未知；测试未下单。不能声称已卖出，也不能以未复核财务遮蔽已知退出规则。

### C09 — 封板附近缺合理成交条件且已追价

- **Verdict：WAIT / Do not chase；Quality cap B；Execution Not implementation-ready。**
- ledger：当前110>原入场上限100且>禁止追价101→G8 Fail；适用封板、区内无法建立入场/成交且同日退出受限→G7 Fail。已有“价格限制临时阻塞”证据，不擅自升级成永久方向不允许G6；不硬编码10%/20%/T+1/100股。
- 原100/95/130方案净RR=(30−0.1)/(5+0.1)=5.862745，只是区内假设；追到110净RR=(20−0.1)/(15+0.1)=1.317881<2，不能靠目标130合理化追价。
- 最小规则：IF 能重新证明有效区99.5–100的合理成交 AND限制/退出/隔夜gap纳入预算、触发成立、首RR≥2 THEN重评；IF >101 THEN WAIT；IF95失效且退出受限 THEN写条件触发/成交受限；重大公告/制度变化重审。
- 心理：用户询问追板本身不能推High FOMO，保持有证据的基线与限制。缺口：实际盘口、成交与隔夜压力损失；外查禁令下只能用提供资料。

### C10 — 财报gap未量化

- **Verdict：WAIT；Quality cap B；Execution Not implementation-ready。**
- ledger：下一交易时段后财报、可能大gap且无法估算、预算无gap情景→G7 Fail；具体event覆盖基线“无near earnings/gap uncertainty”，也使原风险screen对应的事件假设失效。不能因技术好沿用风险通过结论。
- 1-2-3继承0/3；心理依基线。宏观/基本面支持不消除事件风险。
- 最小规则：IF 财报前gap压力损失被量化 AND预算/最小单位/退出能力明确通过 THEN重新研究；否则等待公告后可验证价格和事实；IF gap破95 THEN旧setup作废、实际执行另核；IF >101 THEN不追；财报后重审订单/现金流论点与结构。
- 缺口：gap大小、压力情景与预算覆盖。使用“下一交易时段后”，不推算未给出的交易日日期。

### C11 — 明确追回亏损与FOMO

- **Verdict：WAIT 新风险；Quality cap B；Risk Warning：纪律门槛失败。**
- ledger：“必须今天赚回昨天亏损”“仓位无所谓”“怕错过”→G9 Fail→暂停新开/加仓。无旧仓，不能因心理风险输出EXIT。
- 心理：Revenge Trading High、FOMO High；“size does not matter”支持忽略风险/Overconfidence风险，但不作人格诊断。总体Emotion Risk High；其他偏差证据不足Unknown。
- 最小规则：IF 仍以追回昨日亏损/怕错过决定规模 THEN不新增风险；IF 重新独立写并接受失效95、预算约束及>101不追规则 AND结构/触发/事件/首RR重新过关 THEN重评，不能仅把口头“冷静”当永久通行证；事件变化重审。
- 1-2-3基线0/3。缺口：可验证的纪律恢复/有效预算承诺；不需要先获取账户数量才能拒绝冲动候选。

### C12 — 第三件事先发生，不能无序凑3/3

- **Verdict：未确认1-2-3；long WAIT；Quality cap B。**
- ①09-22破线 Yes；②失败反弹直到09-28才确认 Yes；③09-23的close92<94发生在②确认前，之后价格96未再破94，因此合格第三项 No/Pending。有效完成度2/3。该顺序不构成Confirmed reversal。
- ledger：时序条件③Fail→没有G4；已有破线/失败反弹→G5→WAIT。
- 输入矛盾：合并后current_price仍100，但structure_event说“自反弹确认后price stayed96”；依指定优先级采用结构事件内最新96，保留冲突记录，不平均两价或把100用于当前RR。
- 最小规则：IF 09-28确认之后有完成日线close<94 THEN补足第三项并重审long；IF 线夺回/新高使旧事件退役 THEN重建；IF新价超有效区/101 THEN不追；事件变化重审。
- 心理依基线。缺口：可靠最新价格/时间待对齐；这个冲突不掩盖已知2/3与WAIT。

### C13 — 有效Bearish 2B，不等于完整主趋势反转

- **Verdict：Bearish 2B 当前有效；long候选 WAIT（Quality cap B），不自动SHORT。**
- 2B：冻结H105；09-22真穿越到106，超过tick0.01；09-23下一完成交易时段close104<105，落在5bars窗口内，满足一次收盘确认；后续未重站106。Bearish，不用量能/follow-through未知补“放量”。
- 1-2-3：输入明确没有完成事件；不能由2B自动写3/3。基线破线第一项仍No，0/3不活跃；只在该条叙述与趋势线基线可兼容的解释下使用，见下方歧义。
- ledger：confirmed bearish false-breakout使多头结构有警告、但不是完整趋势确认反转→G5→WAIT/B；不能机械套G4 AVOID/D。已有多头结构需重审，不承袭旧强setup。Short另需自身入场、极值外失效、目标、借券及预算。
- 最小规则：IF 完成/有效重站穿越极值106以上 THEN该Bearish 2B退役并重审；IF新long结构修复且首RR/风险通过 THEN新候选；IF要做空 THEN先建独立结构/极值外风险位/许可；不得沿用旧>101追价例外；事件变化重审。
- 缺口：重建long/short setup；2B与基线“无failed breakthrough”范围需要明确。局部2B事实不需要伪造整个主趋势反转。

### C14 — 只是接近前高，2B为None

- **局部Verdict：None / 不构成2B；2B本身无降级gate。** 在完全继承其余基线并接受“没有更近障碍”的条件下，全候选仍可为STRONG BUY SETUP / A / Pending；局部问题不意味着已激活交易。
- 2B：前高105、最大104.99<105，完整OHLC证明没有穿越；收回104不能补出先决穿越。不是Possible，也不是因缺数据的Unknown。1-2-3继承0/3。
- ledger：2B穿越条件Fail→无2B；这只否定该形态，不证明其它所有买入gate通过。心理不从“碰前高就跌”的提问猜偏差。
- 最小规则：IF后续真实极值超过105且超过tick/噪声 AND在5bars内完成close<105 THEN重新判断Bearish 2B；IF无穿越 THEN不标2B；全候选仍受基线入场、95作废、>101不追与事件重审限制。
- 缺口：无此2B证据缺口；基线风险仅为合成条件screen，不给实际下单/数量。

### C15 — 空头研究通过；仓位保护规则有张力

- **研究Verdict：SHORT SETUP（不是BUY），Trigger Pending；Quality B+，心理未充分评估cap A-；Execution Conditional。** 不给具体仓位方案；若把risk-reward的绝对封顶文字解释为所有空头执行硬门槛，则执行端必须WAIT，见缺陷。
- 周/日LH110→104、LL100→90，下降线保持，Risk-Off；给定没有bullish reversal。1-2-3的逐项日期/线值未展开，因此完成度Unknown/无已证实的完整多头反转；2B Unknown。不能由“no bullish reversal”伪造三步各项No。
- ledger：Short stop104>entry100>target90→G2 Pass；grossRR2.5、netRR2.414634≥2→G3/G8 Pass；提供借券/成本/拥挤/成交及退出capacity、方向许可、条件情景预算→研究风险screen通过；不以普通止损声称绝对亏损封顶。没有账户数量不阻塞研究。
- 评分采用90/90/80/90/85/85/90/Unknown，贡献18/13.5/16/9/12.75/4.25/9/0=82.5，Coverage95%，区间[82.5,87.5]，下界B+，再受心理未知A- cap。基本面与催化只有摘要，故不凭“complete”任意评95。
- 心理：数据只写“known low emotion risk”，没有用户陈述/六类依据，按心理参考严格标Not enough information，不默认Low。提供可审查的当前自述后可重新评分，仍不保证Strong。
- 最小规则：IF下一完整日线close<100 AND实际价格仍在新定义的有效入场区域、不得追到<99、borrow/carry/exit/事件与首RR≥2仍通过 THEN研究SETUP ACTIVE；IF风险价104触发 THEN作废但stop不封顶；IF<99 THENWAIT；催化/借券召回/挤空变化立即重审。没有限定损失保护时不输出绝对封顶的仓位方案。
- 缺口：交易所/币种/时区未给，报告Unknown，不能继承被整包替换的Alpha元数据；波段/线/催化日期、明确入场区及心理依据未展开。合成同单位数学可以算，但真实执行前必须补身份与成本/合约单位。受测试只读约束没有读取或执行安装PEI支持流程。

### C16 — 第一目标失败；远目标不能遮蔽

- **Verdict：PASS 当前候选；Quality cap C。**
- ledger：104/95/110第一RR=6/9=0.666667<1→G3 Fail→PASS；125第二RR=21/9=2.333333不能替代首目标，无分批权重不得造加权赔率。并列G8：104>原禁止追价101，继承触发与新入场104冲突；即使重写触发也不能解G3。
- 1-2-3基线0/3；心理没有新增证据，不因用户问远目标推断偏差。
- 最小规则：IF采用Entry104/Stop95/首目标110且无有效分批计划 THENPASS；IF想重评 THEN建立有结构依据的新位置/失效/目标/分配、解除旧触发冲突并以首可执行目标重新过门槛；IF>101仍按旧规则不追；95失效则作废；事件变化重审。
- 缺口：分批分配和路径、新的入场触发。不要人为改紧95，也不要忽略110障碍。没有旧仓，不推导EXIT。

## 独立发现的可用性缺陷、歧义与输入问题

1. **空头绝对损失保护 vs 情景预算的实质张力。** 主Skill写“Short区分绝对损失上限与情景预算”，handoff允许条件risk screen，同时risk-reward写“无已定价限定亏损保护则无仓位方案”。decision-policy的G6/G10没有直接对应这一必需保护gate。C15可读成SHORT SETUP但不给仓位，也可读成执行必须WAIT；两者应以明确的“研究候选/执行姿态/是否需要有界损失”的规则区分，否则不同代理会给不同结论。此次采用研究通过、不给仓位，未声称绝对封顶。
2. **评分仍是自由裁量，Strong标签可漂移。** 八模块只有宽区间提示，没有统一逐项锚点；C01本评91/A且Strong，但另一评估者合理给89/A-就仅BUY。应保留逐项ledger且避免把测试预期写成唯一分数；心理总分如何处理六类部分Unknown也没有明确聚合方法。C15“known low emotion risk”不足还是可当来源评估同样需说明。
3. **已确认Bearish 2B究竟套G4还是G5未写清。** 2B参考明确它不等于1-2-3或主趋势反转，但G4叫“已确认结构反转”，可能包含confirmed 2B。C13此次按G5 WAIT/B；应明确2B独立警告与方向否决的关系和所用周期。
4. **1-2-3第一项No时，后两项应为N/A还是No、以及“未完成”是否可以直接0/3，需统一。** 有完整未破线证据可0/3；仅一句“无完整反转”不能证明三项都No，故C15 Unknown。否则不同模型会滥报0/3。
5. **数据合并缺少Skill原生冲突规则。** 测试特别指明event覆盖基线，Skill只泛称找权威事实。C12具体事件96与合并current100冲突，已按指令采用96；C10事件覆盖风险screen的旧事件前提；C16新的entry104和旧no-chase101冲突应并列报告。实际用户数据需要明确同事件、同时间和字段优先级，否则可能算错当前RR。
6. **C13的基线范围不清。** 基线trendline声称“无failed breakthrough”，而two_b_data给有效前高假突破。若基线该词只指趋势线，则可兼容；若指所有前高/低假突破，则是输入冲突，需以明确新形态事件优先，否则G0应同时报告。此次使用具体、dated的2B事实判断局部形态。
7. **目标与 prior high 的证明摘要有限。** 基线日线高105，但target_basis宣称111是首预验证高周期阻力且没有近端障碍。此次接受合成source pack对“105不构成可执行障碍”的结论；真实使用应说明105已如何消化/为何不先成为目标，不能靠一句“无更近障碍”掩盖价格结构。C02的108与C14仍须同样注意。
8. **触发收复100与入场上限100窄窗口，存在激活可行性问题。** 需要完成收盘收复100，区间却不能超过100；若“收复”严格>100，则无合法成交点。可读成close≥100、后续回测在区内执行，或重定义触发价范围；目前必须按实际价格重算与区间筛选，不能见close100.1就自动ACTIVE。C15也缺明确短头入场区域。
9. **stop边界与成交分开仍有遗漏。** 基线仅写95/intraday，没有strict below还是touch阈值，C08才明确below；C15同样104未定义触发边界。输出中的研究失效和可执行退出必须保留这个Unknown，不能承诺精确stop成交。
10. **handoff的强制读取范围与已提供支持包边界未明确。** 主Skill要求读已安装路由和子Skill，但测试限制只读新Skill及其references。此次明确没有执行handoff，使用给定fact/risk packet作条件支持；Skill应明确“已提供充分用户支持包”是否满足支持输入，避免候选被无关账户preflight或不存在的RPC阻塞。

数学脚本与参考中的四组long/short赔率、成本扣法和分档相符；此次未发现这些输入下的数学错误。以上是实际执行观察，不能推定任何未来调用都会守住所有gate。
