# Risk Management Rules

## Position Sizing
- **Max position size**: never exceed 5% of portfolio per trade
- **Kelly fraction**: use 1/4 or 1/2 Kelly, never full Kelly
- **Volatility targeting**: size positions so portfolio vol = target vol
- **Fixed fractional**: risk X% of portfolio per trade (1-2% typical)

## Drawdown Limits
- **Max drawdown**: stop trading if drawdown exceeds 20%
- **Daily loss limit**: stop if daily loss exceeds 2-3% of portfolio
- **Weekly loss limit**: stop if weekly loss exceeds 5-7% of portfolio

## Leverage
- **Max leverage**: 2x for retail, document margin requirements
- **Margin call buffer**: keep 50%+ margin free
- **Liquidation risk**: never let a single position cause liquidation

## Correlation
- **Max correlation**: no two positions with correlation > 0.7
- **Sector limit**: max 20% in any single sector
- **Asset class limit**: max 50% in any single asset class

## Stop Loss
- **Always define before entry**: never enter without a stop
- **Never move stop against you**: only move to lock profits
- **Stop types**: fixed %, ATR-based, trailing, time-based

## Kelly Criterion
```
f* = (bp - q) / b
where:
  b = odds received on the wager (net odds)
  p = probability of winning
  q = probability of losing (1-p)

Use fractional Kelly: f = Kelly_fraction * f*
  1/4 Kelly: conservative, lower variance
  1/2 Kelly: moderate
  Full Kelly: aggressive, high variance (not recommended for retail)
```

## Risk Metrics
| Metric | Formula | Target |
|--------|---------|--------|
| Sharpe Ratio | (Rp - Rf) / σp | > 1.0 |
| Sortino Ratio | (Rp - Rf) / σd | > 1.5 |
| Calmar Ratio | Rp / MaxDD | > 1.0 |
| Max Drawdown | (Peak - Trough) / Peak | < 20% |
| Win Rate | Wins / Total | 40-60% |
| Profit Factor | Gross Profit / Gross Loss | > 1.5 |
| Recovery Factor | Net Profit / Max DD | > 2.0 |
