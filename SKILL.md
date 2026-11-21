---
name: quant-algo-auto
description: Quantitative investing, algorithmic trading, and automation. Covers channel operations (content planning, scripts, SEO, analytics) and trading assistance (strategy development, backtesting, risk management, code templates). Use when the user asks about quant trading, algo trading, backtesting, strategy development, risk management, position sizing, trading automation, or YouTube channel strategy for finance/quant content.
---

# Quantitative Investing & Algorithmic Trading

Quantitative investing, algorithmic trading, and automation — for both channel operations (content planning, scripts, SEO, analytics) and trading assistance (strategy development, backtesting, risk management, code templates).

## Scope & Routing

This skill has **two distinct sections**. Determine which applies before proceeding:

| If the user asks about... | Go to Section |
|---|---|
| Content planning, scripts, SEO, video structure, channel analytics, publishing | → **Section A: Channel Operations** |
| Strategy development, backtesting, risk management, position sizing, code templates | → **Section B: Trading Assistance** |

Do not mix concerns. If a request spans both (e.g., "make a video about backtesting"), handle the trading part first, then the channel part.

---

## Section A: Channel Operations

## Domain Knowledge

### Content Pillars (YouTube Channel)
1. **Backtesting & Validation** — walk-forward optimization, overfitting, Monte Carlo, out-of-sample testing
2. **Strategy Implementation** — vectorbt, Freqtrade, Pine Script, QuantConnect/LEAN, Python
3. **Risk & Position Sizing** — Kelly criterion, max drawdown, VaR, position sizing, correlation
4. **Market Microstructure & Factors** — slippage, transaction costs, factor investing, volatility risk premium

### Trading Concepts
- **Alpha vs Beta**: excess return vs market return
- **Sharpe/Sortino/Calmar ratios**: risk-adjusted performance
- **Max Drawdown**: peak-to-trough decline
- **Kelly Criterion**: optimal bet sizing (f* = (bp - q) / b)
- **Walk-Forward Optimization**: train on past, test on future, roll forward
- **Overfitting**: curve-fitting to historical data, fails on new data
- **Transaction costs**: commissions, slippage, market impact
- **Survivorship bias**: only surviving stocks in historical data
- **Look-ahead bias**: using future data in backtest

### Code Stack
- **Python**: pandas, numpy, vectorbt, backtrader, zipline, quantstats
- **Rust**: for low-latency execution, HFT
- **Freqtrade**: crypto algo trading framework
- **Pine Script**: TradingView strategies
- **QuantConnect/LEAN**: multi-asset algo platform
- **Blender**: 3D visualization for channel content (pairs with blender-* skills)

### Content Calendar (Weekly 1 Video, ~10 min)

| Week | Pillar | Topic Template | 10-min Structure |
|------|--------|----------------|------------------|
| A | Backtesting | "How to avoid overfitting: Walk-Forward Optimization" | Problem → Method → Code demo → Conclusion |
| B | Implementation | "Backtest a dual MA strategy in 10 min with vectorbt" | Concept → Code → Results → Pitfalls |
| C | Risk | "Kelly Criterion: from formula to code" | Theory → Implementation → Stress test |
| D | Microstructure | "How slippage & fees eat your alpha" | Phenomenon → Quantify → Mitigate |

### 10-Minute Video Template
```
0:00-0:30  Hook (problem/pain point, specific number)
0:30-1:30  Concept (1 core idea)
1:30-6:00  Code demo (screen recording, step-by-step)
6:00-8:00  Results + common pitfalls
8:00-9:00  Summary + next week preview
9:00-10:00 CTA (subscribe/comment/download code)
```

### SEO Title Formula
`[Concept] + [Tool] + [Promise/Result]`
- "Walk-Forward Optimization: Validate your strategy with Python"
- "Kelly Criterion in algorithmic trading: from formula to code"
- "Freqtrade tutorial: run your first strategy in 10 minutes"

### Tags (5-8 per video)
`quantitative trading`, `algorithmic trading`, `Python`, `backtesting`, `Freqtrade`, `vectorbt`, `Kelly Criterion`, `automated trading`

### Production Workflow (Weekly)
| Day | Task |
|-----|------|
| Mon | Topic selection + script outline + code |
| Tue | Record code demo + narration |
| Wed | Edit + subtitles + thumbnail |
| Thu | Review + schedule (publish Fri 18:00) |
| Fri | Publish + community engagement |

### KPIs (review every 4 weeks)
- CTR > 5%
- AVD > 50% (10 min → 5+ min)
- Subscribe conversion > 2%
- Comment rate > 1%

### Differentiation
- **Research hygiene**: emphasize "how to validate" not "what to buy"
- **Reproducible code**: every video links to GitHub repo (code + notebook)
- **Chinese market**: very few Chinese quant channels, first-mover advantage
- **Honest results**: show real slippage/fees/overfitting, don't sugarcoat

## Section B: Trading Assistance

### Strategy Development Checklist
1. Define hypothesis (what edge, why does it exist)
2. Select universe (assets, time frame, frequency)
3. Define entry/exit rules (precise, no ambiguity)
4. Define position sizing (Kelly, fixed fractional, volatility targeting)
5. Backtest with realistic costs (commissions, slippage, market impact)
6. Out-of-sample test (walk-forward or held-out period)
7. Monte Carlo simulation (drawdown distribution)
8. Paper trade (live but no real money)
9. Live trade (small size, monitor)

### Risk Management Rules
- **Max position size**: never exceed 5% of portfolio per trade
- **Max drawdown limit**: stop trading if drawdown exceeds 20%
- **Kelly fraction**: use 1/4 or 1/2 Kelly, never full Kelly
- **Correlation check**: ensure positions are not highly correlated
- **Leverage**: max 2x for retail, document margin requirements
- **Stop loss**: always define before entry, never move it against you

### Backtesting Checklist
- [ ] No look-ahead bias (use only data available at decision time)
- [ ] No survivorship bias (include delisted stocks)
- [ ] Realistic transaction costs (commissions + slippage)
- [ ] Out-of-sample period (at least 30% of data)
- [ ] Walk-forward optimization (not just in-sample)
- [ ] Monte Carlo simulation (1000+ paths)
- [ ] Parameter sensitivity (does it work across params?)
- [ ] Market regime coverage (bull, bear, sideways)
- [ ] Liquidity check (can you actually trade this size?)

### Code Templates
See `references/` and `scripts/` for:
- `strategy_template.py` — Python strategy skeleton (vectorbt)
- `backtest_checklist.md` — validation checklist
- `risk_rules.md` — risk management rules
- `content_plan.md` — 12-week content plan template

## External Trust Anchors
- **Blender MCP** (if using blender-* skills for 3D visualization): external binary, not bundled
- **Freqtrade**: external framework, install via pip
- **QuantConnect/LEAN**: external platform
- **YouTube Data API**: requires API key for analytics

## Guardrails
1. Never present backtested returns as guaranteed future performance.
2. Always disclose limitations (overfitting, survivorship bias, look-ahead).
3. Never recommend specific stocks/securities as investment advice.
4. Always include risk disclaimers in video content.
5. Paper trade before live trading; start small.

## References
- `references/content-plan.md` — 12-week content plan template
- `references/backtest-checklist.md` — backtesting validation checklist
- `references/risk-rules.md` — risk management rules
- `scripts/strategy_template.py` — Python strategy skeleton
