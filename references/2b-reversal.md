# 2B / False Breakout

出处核验：[Victor Sperandeo，Wiley《Trader Vic on Commodities》Chapter 4, 2B or Not 2B: A Classic Rule Revisited](https://doi.org/10.1002/9781119196792.ch4)。出版商摘要确认突破前高不能延续并回落及其镜像。窗口/容差/收盘条件是本系统约定，不沿用摘要的概率断言。

Bearish：冻结已确认重要前高H；记录超过H+buffer的真实穿越；在two_b_window_bars内按配置次数收盘回到H-buffer以下。穿越不超过tick/噪声不确认。穿越和收回须有先后；单根OHLC无法判定盘中路径时至少等后续收盘，不能编路径。

Bullish镜像：破已确认前低L，窗口内收盘重回L+buffer上方。量能/follow-through辅助，未得数据不说放量。

状态 Bullish/Bearish/Possible/None/Unknown：Possible=已穿越等待收回；None=证据完整无合格事件；Unknown=缺数据。窗口外才回到水平不算本次有效2B；接近前高失败但未穿越不确认。

给 level、穿越日期/极值、收回日期/收盘、窗口/容差、失效条件。Bearish重站穿越极值之上、Bullish再破穿越低点时退役/重审。可在极值外合理缓冲讨论反转候选失效，但仍要入场/目标/预算，不自动BUY/SHORT。

2B自身不是1-2-3的3/3，也不是主要趋势确认反转；标当前有效/退役，避免重复保留已失败信号。
