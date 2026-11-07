#!/usr/bin/env python3
"""
Strategy Template — Quantitative Trading Skeleton

Usage:
    python strategy_template.py --symbol AAPL --start 2020-01-01 --end 2024-12-31

Dependencies:
    pip install vectorbt yfinance pandas numpy
"""

import argparse
import numpy as np
import pandas as pd
import vectorbt as vbt
import yfinance as yf


def fetch_data(symbol: str, start: str, end: str) -> pd.DataFrame:
    """Fetch OHLCV data from Yahoo Finance."""
    df = yf.download(symbol, start=start, end=end, auto_adjust=True)
    if df.empty:
        raise ValueError(f"No data for {symbol}")
    return df


def generate_signals(df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Generate entry and exit signals. Replace with your strategy logic."""
    # Example: dual moving average crossover
    fast = df["Close"].rolling(10).mean()
    slow = df["Close"].rolling(30).mean()

    entries = (fast > slow) & (fast.shift(1) <= slow.shift(1))
    exits = (fast < slow) & (fast.shift(1) >= slow.shift(1))

    return entries, exits


def run_backtest(df: pd.DataFrame, entries: pd.Series, exits: pd.Series) -> vbt.Portfolio:
    """Run backtest with realistic costs."""
    portfolio = vbt.Portfolio.from_signals(
        df["Close"],
        entries,
        exits,
        init_cash=10000,
        fees=0.001,          # 0.1% commission
        slippage=0.0005,     # 0.05% slippage
        freq="1D",
    )
    return portfolio


def print_results(portfolio: vbt.Portfolio) -> None:
    """Print backtest results."""
    print(portfolio.stats())
    print(f"\nTotal Return: {portfolio.total_return():.2%}")
    print(f"Sharpe Ratio: {portfolio.sharpe_ratio():.2f}")
    print(f"Max Drawdown: {portfolio.max_drawdown():.2%}")
    print(f"Win Rate: {portfolio.trades.win_rate():.2%}")
    print(f"Profit Factor: {portfolio.trades.profit_factor():.2f}")
    print(f"Number of Trades: {portfolio.trades.count()}")


def main():
    parser = argparse.ArgumentParser(description="Quantitative Strategy Backtest")
    parser.add_argument("--symbol", default="AAPL", help="Ticker symbol")
    parser.add_argument("--start", default="2020-01-01", help="Start date")
    parser.add_argument("--end", default="2024-12-31", help="End date")
    args = parser.parse_args()

    print(f"Fetching data for {args.symbol}...")
    df = fetch_data(args.symbol, args.start, args.end)

    print("Generating signals...")
    entries, exits = generate_signals(df)

    print("Running backtest...")
    portfolio = run_backtest(df, entries, exits)

    print("\n=== Results ===")
    print_results(portfolio)

    # Plot
    # portfolio.plot().show()


if __name__ == "__main__":
    main()
