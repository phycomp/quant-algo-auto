# Backtesting Validation Checklist

## Pre-Backtest
- [ ] Hypothesis clearly defined (what edge, why it exists)
- [ ] Universe defined (assets, time frame, frequency)
- [ ] Entry/exit rules precise (no ambiguity)
- [ ] Position sizing method chosen
- [ ] Data source identified (quality, survivorship bias)

## During Backtest
- [ ] No look-ahead bias (only data available at decision time)
- [ ] No survivorship bias (include delisted assets)
- [ ] Realistic transaction costs (commissions + slippage + market impact)
- [ ] Out-of-sample period (≥30% of data held out)
- [ ] Walk-forward optimization (not just in-sample)
- [ ] Parameter sensitivity (works across params?)
- [ ] Market regime coverage (bull, bear, sideways)
- [ ] Liquidity check (can you trade this size?)

## Post-Backtest
- [ ] Monte Carlo simulation (1000+ paths)
- [ ] Drawdown distribution analysis
- [ ] Sharpe/Sortino/Calmar ratios computed
- [ ] Max drawdown within acceptable limits
- [ ] Win rate and profit factor
- [ ] Trade frequency and holding period
- [ ] Correlation with other strategies

## Red Flags
- In-sample Sharpe > 3.0 (likely overfit)
- Win rate > 80% (likely overfit or survivorship bias)
- Max drawdown < 5% (unrealistic)
- Parameter count > 5 (overfit risk)
- No transaction costs modeled
- Single market regime tested
- Look-ahead bias in signals
