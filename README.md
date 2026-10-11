# professional-speculator · 专业投机决策系统

一个用于 Codex / Agent Skills 环境的交易决策 Skill，判断公开证券**现在是否值得交易**。

分别评估公司、资产与当前交易。使用价格结构、1-2-3 / 2B、入场位置、结构失效、风险收益、宏观与基本面确认、风险预算和心理纪律，输出可证伪的条件计划。

## 决策流程

市场 → 行业/证券趋势 → 反转 → 入场位置 → 失效位 → 第一目标赔率 → 确认 → 风险 → 纪律 → 裁决。

硬否决条件优先于评分：没有合理失效位或第一目标赔率不足，当前方案可以得到 PASS；等待结构、价格或事件确认时得到 WAIT；严重数据缺失时得到 WATCH / INSUFFICIENT DATA。BUY SETUP / SHORT SETUP 表示条件候选，触发与实际成交分开。

## 使用

将本仓库内容放入运行环境实际发现的个人 Skill 目录，文件夹命名为 `professional-speculator`，确保直接包含 `SKILL.md`。安装位置以你的运行环境及[官方技能文档](https://learn.chatgpt.com/docs/build-skills)为准。

然后输入：

```text
$professional-speculator 按照专业投机原理分析紫金矿业，判断现在是否值得交易，给出失效位、第一目标赔率和条件化计划。
```

也支持“现在是不是好买点”“是否形成1-2-3反转”“这笔交易赔率如何”等请求。纯长期基本面、商业模式、估值模型或独立组合风险工作由对应专业流程负责。

## 文件与依赖

- `SKILL.md`：入口及决策依赖链。
- `references/`：趋势、反转、gate、心理、市场制度、交接、输出规范及可修改配置。
- `scripts/risk_reward_calculator.py`：仅执行数学计算。
- `tests/`：11项数学回归、17个合成决策案例、独立评估及修复复评。
- `agents/openai.yaml`：中文显示名与自动选择策略。

Python计算器只用标准库。基本面、组合风险、宏观和监控优先复用实际安装的 Public Equity Investing Skills；缺少插件或数据时标注局限并提供有限的条件分析，不虚构 API 或服务调用。充分的用户支持包可作条件输入。

## 验证

在仓库根运行：

```text
python -m unittest discover -s tests -v
python scripts/risk_reward_calculator.py --entry 31.20 --stop 29.80 --target 34 --target 35.80
```

测试使用合成数据。行为评估记录见 `tests/independent-evaluation.md` 和 `tests/independent-recheck.md`；规则预期见 `references/behavioral-cases.md`。复评包含重复案例，不能把两轮数量相加当不同样本。

## 适用范围与限制

支持股票、ETF、指数的结构研究，覆盖A股、港股和美股的市场制度检查。实际执行条件必须按证券及日期核实；指数的真实交易表达须另外明确。

没有内置行情下载或下单功能；缺行情不会编造价格、支撑或目标。普通止损不保证成交价或绝对亏损封顶。评分含分析判断，硬gate优先；测试不保证所有未来模型调用都遵守规则。仓库包含研究流程，不包含账户凭证或个人组合资料。

思想借鉴 Victor Sperandeo；2B出处见 [Wiley 作者章节](https://doi.org/10.1002/9781119196792.ch4)。窗口、阈值和评分为本系统约定，不声称原书精确参数或实证胜率。
