# 趋势与位置

先市场/行业基准，再证券；不同周期分别判断，日线反弹不改写周线下降。Primary=Bull/Bear/Sideways/Unclear；Secondary=Up/Down/Consolidation/Counter-trend rally/Counter-trend correction/Unknown；Market Regime=Strong Risk-On/Risk-On/Neutral/Risk-Off/Strong Risk-Off/Unknown；Volatility=Elevated/Normal/Subdued/Unknown；Confidence=High/Medium/Low。Risk-On 应由广度/流动性/信用/相关资产证据支撑，不能只看个股涨幅。

波段记录 `time | high/low | price | source | timeframe | confirmed_at`。默认两侧各 pivot_confirmation_bars 根较低高点/较高低点确认 swing，可用披露的方法替换；历史判断不能使用尚未出现的右侧K线。等高低为 Equal，不强行 HH/LL。两个已确认高点+两个低点构成最小方向证据，少量K线不自动证明主趋势。

- HH+HL=uptrend；LH+LL=downtrend；混合/相等=range/transition；不足=Unclear。
- HH/HL/LH/LL 分别 Yes/No/Unknown 并给波段点位，不能只凭叙述。
- 上涨线用至少两个有效低点、下降线用至少两个有效高点；同周期、不同时间，注明线性/对数及锚点日期价格。不能为迎合信号临时重画；无有效线=Unknown，仅两点可信度有限。
- 支撑/阻力给区间、形成/检验日期、突破/失败证据，整数位不自动是支撑。

Strength=Strong/Moderate/Weak/Unknown；Condition=Trend intact/Trend weakening/Trend under pressure/Possible reversal/Confirmed reversal/Unclear。Bull+Low可能结构开始恶化，方向和确定性分开。

Trade Location：固定周期、支撑阻力、入场区、失效，算到支撑/失效/首障碍的距离；历史波动辅助须有来源，不凭空算ATR。Long入场区上端、Short下端是较差RR。支撑不自动是止损，缓冲要考虑噪声/tick。

Excellent=靠近合理失效且空间充足；Good=距离可控+可验证触发；Acceptable=仍过预算/赔率；Poor=远离结构、剩余空间不足或追价；Very Poor=已过目标/明显追价/失效无法设置。百分比不是通用标准，说明具体依据。

突破、回踩、续行、反转新结构分别写触发。强趋势不提高坏位置评分；价格超不追价边界就取消旧触发，等待新位置。
