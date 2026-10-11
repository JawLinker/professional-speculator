# 已安装 Public Equity Investing 的交接

交接规范已针对 Public Equity Investing 插件验证。使用时从当前会话 skills catalog 定位实际已启用的 `public-equity-investing/SKILL.md`，取其父目录的兄弟 Skill；插件根按该安装结构解析，不依赖开发机器路径或固定版本。skills:// 资源标识不是通用本机文件路径；按实际提供的读取机制处理。不要凭版本号猜路径或挑未启用缓存版本。

先读路由器，再读插件根 `shared/invocation-policy.md`、`shared/plugin-routing-playbook.md`；支持工作遵守 router Cross-Skill Runtime Contract 和选中 Skill 的 source resolution。首次借用新交付流程读 `shared/final-deliverable-framework.md`、`shared/deliverable-intake-policy.md`；不要自动运行 user-context preflight。

子Skill的 agents/openai.yaml 在此安装采用显式调用策略。路由器明文允许读取并使用精确安装的子Skill文件；这是同一代理执行支持工作，并非存在独立技能RPC。无可调用工具不要写“已调用/已返回”。工具必须实际发现、读成功才能称可用。不能将 .app.json 的类别当已连接服务。

## 所有支持包共用字段

`request_id, security/exchange/currency, as_of/timezone, direction, horizon, position_status, decision_question, source_inventory, known_unknowns, requested_output_slice, resolved_surface/depth`。接收结果时带回来源时间、事实/假设/推导、局限、ready/conditional状态、未解冲突；未经证据不得复制目标价/胜率。

默认新Skill的紧凑决策卡为已解决的交付形态。将子Skill明确设为本决策卡的**支持输入**，继承现有格式/深度，不触发每个子Skill整份HTML/XLSX或重复询问。用户另要求独立长短报告、估值模型、风险包/追踪表时，恢复对应owner及其完整交付/验证规范。

用户已经提供足够、时点一致的事实/风险包时，先抽取并标 `Provided support packet`，无需为了产生一次新handoff而重复已完成的支持研究。真正需要新增owner工作才读取其流程。提供包不能免除本Skill的证据、时序、事件、预算与执行gates，也不证明当前连接器可用。

| 需求 | 读取 `skills/<id>/SKILL.md` | 发送的补充输入 | 要回的切片 |
| --- | --- | --- | --- |
| 身份与事实基线 | company-tearsheet | 所需财务期间、关键暴露 | 公司/资产基线、来源、关键驱动/风险，非买入评级 |
| 缺交易论点/反方论据 | long-short-pitch | 候选表达、价格锚、失效、事件路径 | Variant perception、为何现在、反证、独立Thesis invalidation；不重做技术结构 |
| 风险/仓位 | portfolio-risk-management | Entry/Invalidation、risk%、quality/confidence、催化剂、波动、现有敞口、预算解释、交易制度、执行未知 | 条件仓位框架、预算、binding constraint、scenario P&L、流动性/退出、add/trim/exit、readiness |
| 具体宏观/政策冲击 | economic-impact-report | 已核实事件、币种/商品/行业暴露 | 传导→财务/估值/资金影响、Macro/Policy/Liquidity、确认/背离、观察证据 |
| 场景/敏感性 | scenario-sensitivity-generator | 已有基准、价格/事件场景及来源 | 压力与门槛，不重建估值或编概率 |
| 候选生成 | idea-generation | 宇宙/筛选条件 | research candidates，不将筛选排名当BUY |
| 财报前后 | earnings-preview / earnings-deep-dive | 已验证日期、预期/实际资料 | 事件gap风险、核心指标、驱动/证伪，不扩成不必要的完整报告 |
| 长期全面研究 | initiating-coverage | 研究范围 | 原owner主导；本Skill只在用户需要交易叠层时附加 |
| 持续状态/日志 | thesis-tracker | trade_id、原论点、交易失效与基本面证伪分开、条件规则/来源/时点、事件、旧裁决 | append-only确认/否定证据、稳定ID、状态变化、下一review及exit/re-underwrite规则 |

风险输入不完整时，允许owner返回 conditional screen，不冒充精确数量；止损计划与gap压力损失分开；Short绝对封顶需限定损失保护或无仓位。风险owner可以更保守地否决，不能以基本面支持撤销本Skill的结构/赔率veto。

监控handoff每条记录：`rule_id, trade_id, metric/source, threshold, timeframe/confirmation, trigger/action, expiry/review_at, threshold_origin`。没有日期别编财报日；新起草条件标 Draft，不伪称 Approved。仅在用户要求更新tracker时写入，保留原始假设/旧判定；仅在用户要求持续监控时使用实际自动化工具，不暗中启动。

依赖缺失/不可读取：说明具体 gap。基本面/宏观从可用公开或用户证据给有限确认；风险仅用 risk-reward.md 的轻量条件框架；记录 unmet handoff，不虚构风险服务已完成。不要改插件缓存/公共router配置，避免升级覆盖与路由污染。

## 与现有技能的边界

现有long-short-pitch已有交易表达、赔率/退出；新逻辑只增加跨周期HH/HL证据、时序1-2-3、2B窗口、位置/失效gate、心理证据和最终裁决优先级。现有risk负责组合约束/对冲；macro负责冲击传导；tracker负责持久证据。纯DCF/商业模式不加载本Skill；只问赔率可只用数学/位置，不强制全部handoff。
