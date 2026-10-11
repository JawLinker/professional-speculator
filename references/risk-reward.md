# 失效、赔率与最小风险框架

Trade invalidation=交易结构/假设坏了；Thesis invalidation=长期驱动证伪；Stop execution=何时尝试成交。失效可价格或事件，但价格RR另需可量化风险价格。只有“基本面不好就卖”而无风险价格→RR unavailable，不通过开仓gate。

Long：风险=Entry−Stop，收益=Target−Entry；Short：风险=Stop−Entry，收益=Entry−Target。百分比除以Entry×100；RR=收益/风险。同币种每股/份all-in成本C：净风险=风险+C，净收益=收益−C，净RR=净收益/净风险。成本未知默认0仅称gross/zero-cost，不能称已验证实际净赔率。

31.20/29.80/34.00→风险4.4872%，收益8.9744%，RR2.00；35.80→收益14.7436%，RR3.2857。不能只报第二目标掩盖第一目标门槛。

分档来自defaults：<1 Very Poor；[1,1.5) Poor；[1.5,2) Acceptable；[2,3] Good；>3 Excellent。四个递增正上界可配置。候选门槛独立于分档。

多目标逐个gross/net RR。明确分配且权重和1才可讨论加权潜在收益，并考虑未全部到达路径；没退出计划不虚构权重。到目标前有更近障碍先处理。区间用最不利端，价格变后重算。

RR不是胜率/预期收益。二元全额结算盈亏平衡概率=net risk/(net risk+net reward)，仅净收益>0时适用；不据此假设正期望。

风险owner不可用/账户未知时只给 `Conditional position framework / Not implementation-ready`。若预算B、每单位损失L明确，数量≤floor(B/L)，按lot/资金/敞口/流动性取更紧约束；不编账户/1%预算。stop不是保证，跳空、封板、T+1、停牌可能损失更大；压力情景交给风险owner。

Short必须核实借券、召回、挤空、成本与许可。**仅当用户要求绝对亏损上限**时，没有已定价限定亏损保护就给无仓位方案；普通stop不满足绝对封顶。明确使用情景损失预算且风险owner已检查借券/挤空/流动性/敞口等时，可给条件SHORT SETUP和相应风险框架，注明情景外损失可超过预算。预算解释未明且会改变方案时才询问，或并列两分支，不把情景预算偷偷当绝对上限。指数本身不能下单，需明确ETF/期货等表达；衍生保证金/合约/期权模型交相应owner，不用现货RR冒充。

运行：`python scripts/risk_reward_calculator.py --entry 100 --stop 105 --target 90 --direction short --cost-per-unit 0.5`。配置默认 references/defaults.json，可 `--config path.json`。NaN/Infinity、非正价格、错向stop/target、负成本、错误配置非零退出。
