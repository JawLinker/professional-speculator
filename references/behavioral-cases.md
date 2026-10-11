# 行为验收（不是实盘回测）

原始输入位于 `../tests/forward_requests.json`。读取common_packet后按changes覆盖，replace_packet整包替换；未列出的原字段保留，额外event/structure_event/rule是重要证据。证券/价格均合成，禁止用作真实推荐。

评估输入只给SKILL.md、其参考、forward_requests，不给本文件预期，避免答案泄漏。要求每例：状态、质量cap、1-2-3/2B、决定性gate、心理依据、IF/THEN及缺口；只报数学通过不等于行为通过。

| Case | 不可违反的结果 |
| --- | --- |
| C01 完整上涨+合理位置/赔率 | BUY SETUP或更强候选，Trigger Pending；不能直接下单或给未经请求账户数量 |
| C02 完整上涨但RR0.8 | PASS；Good company不解禁G3，最多C |
| C03 同事件顺序3/3+持仓 | 本周期Confirmed reversal；旧仓规则触发EXIT，新增多头AVOID |
| C04 2/3 | weakening/Possible reversal；不能confirmed |
| C05 好基本面坏结构 | WAIT；明确公司与交易不同 |
| C06 有数据无可定义失效 | PASS，最多C，不编stop |
| C07 关键数据缺 | WATCH+INSUFFICIENT DATA、Unrated，不编点位/RR/财务 |
| C08 成本锚+失效 | Anchoring/Sunk Cost有语句依据；规则触发EXIT，不能成本等回本 |
| C09 涨停附近无法合理入场 | WAIT/Do not chase；不保证成交/盘中止损 |
| C10 临近财报gap不可估 | WAIT；好技术不能解禁G7 |
| C11 明确revenge/FOMO | WAIT新增风险+有证据Risk Warning，不诊断人格 |
| C12 第三事件在第二确认之前 | 不得凑3/3；需后续同事件确认，最多2/3有效顺序 |
| C13 真穿越后窗口内收回 | Bearish2B；不直接宣称主趋势反转/自动做空 |
| C14 未穿越 | None，不确认2B |
| C15 完整空头输入 | SHORT SETUP（RR/等级过门槛时）；否则WAIT且明确成本后RR门槛，不用BUY标签 |
| C16 近端RR不足远端好 | 首目标RR=6/9<1→PASS；不能只挑远端目标 |
| C17 空头绝对损失上限无保护 | PASS当前表达/无仓位方案；普通止损不能满足绝对封顶，情景预算不能偷偷替代 |

进一步边界：无心理信息必须Unknown/Not enough information；财务强但RR差仍PASS；同股票只改入场价就可能从SETUP变PASS；MACD金叉不解禁结构反转；Unknown流动性/borrow不成为implementation-ready。已有仓位RR差不自动EXIT，只有失效/组合风险足够证据才决定旧仓动作。

路由例：触发“按照专业投机原理分析紫金矿业”“现在是不是好买点”“1-2-3确认了吗”“给条件化交易计划”；不触发“苹果商业模式是什么”“做一个完整DCF”“仅建组合风险模型”。后两者交原owner，本Skill可作用户明确要求的叠层。

验证等级分开：格式/链接检查、自动数学回归、人工规则走查、独立模型行为测试、真实市场来源测试。没有执行的层级明确记为未执行；独立测试给出的分数/标签偏差要依据gate复核，不靠字符串匹配证明决策正确。
