# 独立修复复评：C01/C12/C13/C14/C15/C17

日期：2026-10-11。此报告追加独立复评，不修改先前报告、Skill或输入。重新阅读当前SKILL、decision-policy、risk-reward、output-contract、1-2-3、psychology、handoff、defaults、2B及raw forward_requests；没有阅读behavioral-cases、预期答案或父任务总结。没有浏览、外部服务、真实交易、账户读取、监控或实际PEI handoff。

所有行情均为合成测试资料，Data Status=`Analysis based on provided data / Synthetic`。事实/风险支持包来源为`Provided support packet`，条件使用不等于我调用风险owner。账户数量未请求，不因此拒绝候选研究；实际执行、数量和成交结果均未验证。

## 总体结论

| 例 | 独立复评Verdict | Quality / cap | 决定性判断 | Trigger/执行 |
|---|---|---|---|---|
| C01 | STRONG BUY SETUP；普通BUY也可在有充分评分依据时成立 | 本评91/A；没有触发降级cap | 最差区间Entry100、首净RR2.137255；无反向结构/事件/纪律gate | Pending / Conditional |
| C12 | 未确认1-2-3；long WAIT | cap B | 第三项发生在失败反弹确认前；只有有效2/3，G5 | 不激活 |
| C13 | Bearish 2B有效；long WAIT | cap B | 105→106真穿越，下一完成收盘104收回；明确只G5，不直接G4 | 旧强setup重审 |
| C14 | None / 不构成2B | 局部形态无需质量评分；候选在其余基线成立时仍A/Pending | 104.99从未穿越105 | 无2B带来的激活/降级 |
| C15 | SHORT SETUP | 本评82/B+；Coverage95%；心理未知cap A- | Short区间最差99.5的净RR2.043478；明确情景预算而非绝对上限 | Pending / Conditional |
| C17 | PASS当前裸空表达；无仓位方案 | Quality cap C；不为局部风险问题强造完整分数 | 要求任何情况绝对封顶、只有普通stop，无已定价限定保护→G6 | 不可执行，不自动EXIT |

## C01：修复后确认和区内入场可以衔接

身份SYNTH.A Alpha / Synthetic equity venue / test units，long、无仓位，截至2026-09-30 16:00 Asia/Shanghai。周线主趋势、日线setup、数周周期。

市场和行业周线高低点上升，Risk-On / Normal / High confidence；证券日线低90→95、高97→99，HH/HL。已确认高99低于当前100，结合给定“111首高周期阻力、无更近障碍”支持Good/Excellent location，不再出现原高105尚未处理的基线障碍。预选线85（07-10）→95（09-10）完整后续无有效收盘跌破。

- 1-2-3：①No，②/③Not applicable；0/3 / Not active。此结论来自完整未破线证据，不能只拿“没完整反转”当理由。2B独立路径Unknown，不能由0/3推出None。
- Company：Strong Positive；Asset：上行趋势、市场行业同向；Trade：失效明确、位置和第一目标赔率通过，三者分开。
- Macro/Policy/Liquidity均Positive，合成支持包机制为订单/融资改善；综合Strong。财务驱动为订单/现金流改善、保守杠杆；催化产品里程碑4周后。Thesis invalidation是持续订单结构性下降，与Trade失效95分列。
- ledger：G0核心证据充分→Pass；G1失效HL95明确→Pass；G2几何与目标依据→Pass；G3首净RR≥1且G8 setup最低RR≥2→Pass；G4/G5无已知反向结构→Pass；G6给定风险/流动性/许可条件screen→Pass（仅条件研究）；G7无临近未量化事件→Pass；G9当前纪律语句支持无极端冲动→Pass；G10已给支持包→研究确认满足。
- 数学：使用多头区间最不利上端100，stop95、C0.1。风险5/net5.1，目标111收益11/net10.9，grossRR2.2/netRR2.137255 Good；目标120 gross4/net3.901961 Excellent，第二目标不替代第一目标。原独立实跑结果仍适用，参数未变。
- 评分：95/95/80/95/95/90/90/90，按20/15/20/10/15/5/10/5权重，19+14.25+16+9.5+14.25+4.5+9+4.5=91，Coverage100%，区间[91,91]，A。评分有分析空间，不为预期Strong反向调分。当前证据采用该分数时可Strong；如果另一个有依据的评分未达90，普通BUY合理。
- 心理：用户明确不追价、不追回亏损、遵守预算/失效且不受成本左右，支持FOMO/Revenge/Anchoring/Sunk Cost Low；Confirmation Bias、Overconfidence Unknown；相关语句足以评本次纪律，总体暂Low。未知项目不能删除或全补Low。

最小IF/THEN：

1. IF 支撑97–98回测守住 AND一个已完成日线close>=100 THEN确认条件完成，但继续等待后续回测。
2. IF后续真实入场/成交条件在99.5–100 AND实际成本后首RR>=2、风险/事件/许可仍有效 THEN研究SETUP ACTIVE；不能把close100.1直接当区内成交。
3. IF可执行盘中价<95 THENHL失效、setup作废/尝试stop执行；95等值不自动满足strict below，且不保证95成交。若以后存在仓位，另列退出风险姿态。
4. IF价>101或成本后首RR<2 THENWAIT/不追；IF订单/政策/产品事件改变核心事实 THEN重审，下一已完成日线及产品事件后复核，不声称已启监控。

修复成立：确认价和后续回踩衔接可行，strict<95明确。证据缺口：具体账户数量、真实通道/成交未知，不影响研究setup；不输出已买入。

## C12：顺序不合格与价格冲突已分开处理

current_price现在明确96，与structure_event一致，原100/96合并矛盾已消失。

1. 09-22破预选趋势线：Yes。
2. 失败反弹101直到09-28才确认：Yes。
3. 反应低94在09-23被close92跌破，发生在第2项确认前；之后价格96未再破94：合格第三项No/Pending。不能把历史92无序拼成3/3。

**Verdict WAIT / cap B**。证据→G5 under pressure/有效2/3→WAIT；没有完整确认反转，不套G4；96也不在99.5–100区内，G8并列阻碍。其他基本面正面不覆盖结构顺序。周线仍可Bull，不能从日线弱化改写周线方向。

心理继承相关明确自述，未因局部形态问题猜新的偏差。2B路径Unknown。

规则：IF09-28确认后出现完成日线close<94 THEN补足同事件第三项、long AVOID并检查旧仓规则；IF线夺回/新高使该事件退役 THEN保留历史并重建；IF价超原追价上限101 THENWAIT；IF催化/订单/政策改变 THEN重审。无旧仓不输出EXIT。

缺口：实际第三项尚未发生，下一完整收盘仍需观察；不编造未来。此处不再有未解当前价冲突。

## C13：具体2B与基线范围已可对齐

**Verdict Bearish 2B有效；当前long WAIT / cap B。**

前已确认重要高105，09-22有效极值106，比105多1，显著超过tick0.01；09-23下一完成交易时段close104<105，位于5bars窗口内并满足一次收盘确认；之后没有重站106，故当前有效。独立量能/持续性未给，Unknown，不能写放量。

ledger：具体dated two_b_data依据更新规则优先于冲突基线概述；本次基线已缩为“没有trendline close breach”，高点假突破与趋势线未破可并存。确认2B本身明确只→G5→WAIT/B；不因confirmed一词直接套G4/D、不自动开空。若以后独立1-2-3或其他方向结构确认，才另用G4。

1-2-3：基线完整证明趋势线第一项未发生，①No/②③N/A、0/3 Not active；不是从two_b_data的“no completed 1-2-3”一句话推出三个No。此0/3与独立Bearish2B能同时成立。心理依基线，提问不证明FOMO。

规则：IF完成有效重站穿越极值106以上 THEN此Bearish2B退役并重审；IF要恢复long THEN重新证明结构/位置/首RR/风险，不继承旧强评分；IF要short THEN独立建立极值外合理失效、入场、首目标、借券/预算；旧>101不追规则仍有效，不能因2B另开例外；事件事实改变重审。

修复成立：2B属于G5已明文；原blanket failed breakthrough范围问题消除。缺口：替代long/short方案和独立反转路径未建立，不用原111/95 mechanically生成反向交易。

## C14：没穿越就没有2B

**局部Verdict None / 不构成2B。** Prior high105，随后最大104.99，完整OHLC证明没有超过105；以后close104不能补先决穿越，不是Possible/Unknown。不能将普通前高受阻说成2B。

ledger：2B穿越Fail→形态None；这不等于任何交易已经激活。若其余基线仍适用，候选可维持A/STRONG BUY SETUP/Pending；局部形态分析本身不需要重做完整评分。1-2-3可依完整未破线基线0/3，不由None推断趋势永远有效。心理无新增证据。

规则：IF以后真实穿越105且超过tick/噪声 AND5bars内完成close<105 THEN重新判断Bearish2B并按G5重审；IF仍未穿越 THEN保持None。买入仍需完成确认后的区内回测，<95作废，>101不追，事件变化重审。

缺口/限制：此局部判定没有穿越证据缺口；two_b_data未提供prior high及later maximum的具体日期/周期，故不补它们，输出日期Unknown。105是否构成当前可执行阻力仍按给定“无更近障碍”的合成支持包接受；真实研究须解释形态高点与首目标之间关系，不能凭本报告声称核验行情。

## C15：情景预算可支持SHORT SETUP，心理不补Low

SYNTH.S / Synthetic equity venue / test units / 截至2026-09-30 16:00 Asia/Shanghai / Short / 无仓位。周、日LH/LL，默认日线setup/数周候选；Security身份、币种和时区不再从替换掉的Alpha包继承。

LH110→104，LL100→90，下降线完整，Risk-Off；基本面Negative支持空头，宏观同向，催化支持；政策/宏观流动性分项未展开，保留Unknown，不把摘要macro agrees造出全部Positive/Negative机制。Asset为下降趋势；Trade可条件通过；“Negative”不单独证明公司永久失败。

1-2-3：不能只从“no bullish reversal”伪报0/3；即使给出anchored falling line intact，该例仍缺逐项日期/线值和完整破线否定路径，所以逐项Unknown/无已证实完整多头反转，known satisfied0、unknown3。2B Unknown。这里Unknown不制造已知反转；完整趋势/源包assertion被合成输入接受，但真实复核要展开序列。

ledger：G1合理风险价104→Pass；G2 short104>有效entry99.5–100>target90→Pass；G3/G8区间最差净RR>=2→Pass；G4/G5没有给定反向确认/under pressure→无已知失败；G6给定borrow/locate/carry/crowding/ADV/exit capacity/许可与情景预算→条件研究Pass；G7/G10使用provided complete风险包，不编外部调用；心理只有标签不足，整个模块Unknown，不直接构成执行veto。

区间最差端要用Short下端99.5，而非只Entry100：

| Entry | 风险 / 净风险 | 首目标收益 / 净收益 | Gross RR | Net RR |
|---:|---:|---:|---:|---:|
| 100 | 4 / 4.1 | 10 / 9.9 | 2.5 | 2.414634 |
| 99.5 | 4.5 / 4.6 | 9.5 / 9.4 | 2.111111 | 2.043478 |

99.5一行本次重新实际运行bundled Python计算器；100一行沿用同参数先前实跑结果。都Good且达到setup2门槛；费用变动后必须再算。普通stop不保证104成交，情景外亏损可以超过给定预算，不能把4.6写成绝对最大损失。

评分按90/90/80/85/85/85/90/Unknown，贡献18+13.5+16+8.5+12.75+4.25+9=82。Coverage95%，区间[82,87]，下界B+；心理未知cap A-不把B+抬高。宏观给85体现仅摘要支持的限制；如将重要未展开确认施加B+ cap，结论仍B+。**Verdict SHORT SETUP / Pending / Conditional**，不称Strong或BUY。

心理：明确只有“known low emotion risk label without raw user statements”→Not enough information，六类及整体Unknown；既不补Low，也不凭Unknown暂停所有研究。提供充分本次预算、退出和追价原始语句后才可评分。

规则：IF下一完整daily close<100 AND之后实际价可在99.5–100成交、更新首RR>=2、借券/carry/退出/事件/情景预算仍通过 THEN研究SETUP ACTIVE；IF盘中可执行价>104 THEN失效/尝试stop，不保证104成交；IF<99 THEN不追，99–99.5之间也因区外不激活；IF借券召回、挤空/事件/基本面变化 THEN重新审风险和结构。没有具体数量，给条件框架；没有要求绝对封顶，不强制限定亏损保护。

修复成立：绝对cap与情景预算区分、区间最差RR、入场区、时区及strict>104都可明确执行。缺口：支持包没有展示全部日期/源证据、政策与流动性宏观分项、原始心理语句、具体仓位；如用于真实执行须补足，不假称风险handoff完成。

## C17：普通stop不满足“任何情况下”绝对亏损上限

**Verdict PASS当前普通止损裸空表达；无仓位方案；Execution Not implementation-ready。** 没有旧仓，不输出EXIT。Good赔率不能解锁绝对风险约束。

ledger：用户请求明确任何情况下不可超过绝对亏损上限；execution明确只有ordinary stop、无priced defined-loss protection→G6 Fail→PASS该表达。普通stop可因跳空、挤空、召回、流动性而损失超过预算。不能用“数量×4.1”或情景压力亏损冒充绝对上限。

数学结构同C15，区间99.5–100、104stop、90目标、成本0.1，最差净RR2.043478；RR通过与风险表达失败同时成立。1-2-3只写没有opposing confirmed reversal，不足判三项No，Unknown；2B Unknown。

Quality：本例局部问绝对封顶且G6已否决，完整评分没有必要；最后再次读取的policy现已明确G6当前表达最多C，故记录Quality cap C，不能用潜在高技术分掩盖不可执行。评分再高也PASS。心理confirmation的“adequate user discipline statements”只是一句包摘要，未提供语句/行为，依修订心理规则仍Not enough information/模块Unknown；绝对风险偏好本身不是FOMO或overconfidence证据。这个Unknown不掩盖G6已知失败。

规则：IF仍要求任何情况绝对封顶 AND只有普通stop THENPASS/无仓位；IF取得已定价有界损失保护 THEN独立重建其价格、成本、首目标、结构、最大损失和许可/预算，不把现货RR直接套期权/衍生表达；IF用户明确将约束改为情景预算 THEN可以另建条件候选，但不能未经明确修订暗改风险需求；新表达的失效、追价阈值、事件重审都须重新定义。当前>104只是普通stop失效条件，不是绝对保护。

缺口：绝对上限金额未提供，但“只有普通stop且无保护”已经足以拒绝现有表达，不必先问金额才下结论；保护instrument、报价、合同损失边界、原始心理信息未知。

## 修复验收与保留限制

以下修复在实际复评中成立：

- confirmed2B只G5，独立confirmed方向反转才G4，C13不再出现AVOID/D争议。
- Short仅当明确绝对cap才必须已定价有界保护，C15条件研究通过，C17明确PASS；不假称普通stop封顶。
- 1-2-3完整第一项No可0/3+N/A，与仅“无完整反转”摘要分开，C01/C13与C15/C17判法可区分。
- 用户充分支持包可以条件使用，无需为了展示handoff而重复研究，也不假称已执行。
- C01收盘确认与后续区内回测、strict<95；C15区内Short及strict>104可清楚写规则。
- C12价格96对齐；基线97→99高点修复原105与首阻力111的问题；评分验收不强求唯一Strong。
- 复评期间最后更新的G2/G6 cap已再次读取确认：无效方案/不可执行表达最多C，无法计算则Unrated；C17 now PASS/cap C，原cap空白已解决。

没有发现新增数学错误。仍有以下具体局限，但不改变上述六例的决定性Verdict：

1. C17的心理“adequate ... statements”没有实际语句，按新规则仍Unknown。若希望测试“充分心理证据”的分支，需真实提供测试语句；不能让测试摘要凌驾证据要求。
2. 支持包摘要仍省略不少逐项来源/日期，尤其C14高105的时间周期、C15线条日期/催化日期/宏观机制。合成provided事实可支持这次局部或条件研究；真实使用必须按G0/G10检查展开资料，不能将“complete”当万能豁免。
3. SETUP ACTIVE仍是研究条件状态，不是实际下单或成交日志。报告没有宣称任何实际买卖/监控/handoff已经发生。
