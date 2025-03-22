import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import streamlit as st


# Calculate required time frame
def timeframe_default(start_date=None, end_date=None):
    if start_date is None:
        start_date = date.today() - relativedelta(years=10)
    if end_date is None:
        end_date = date.today()

    return start_date, end_date


# =============================================
# Short-Term Indicators (Days to Weeks)
# =============================================

# RSI (Relative Strength Index)
# Meaning: Measures if stock is overbought (>70) or oversold (<30).
# Bullish: RSI moves above 30 (from oversold).
# Bearish: RSI moves below 70 (from overbought).
def calculate_short_term_RSI(df, window=14):
    pass  # Implement calculation here

# Stochastic Oscillator
# Meaning: Measures closing price relative to recent range.
# Bullish: %K crosses above %D.
# Bearish: %K crosses below %D.
def calculate_stochastic_oscillator(df, k_window=14, d_window=3):
    pass  # Implement calculation here

# VWAP (Volume-Weighted Average Price)
# Meaning: Shows the price weighted by trading volume.
# Bullish: Price moves above VWAP.
# Bearish: Price moves below VWAP.
def calculate_VWAP(df):
    pass  # Implement calculation here

# Short-Term Moving Average (9-20 days)
# Meaning: Identifies short-term price direction.
# Bullish: Price crosses above short-term MA.
# Bearish: Price crosses below short-term MA.
def calculate_short_term_MA(df, window=9):
    pass  # Implement calculation here

# =============================================
# Medium-Term Indicators (Weeks to Months)
# =============================================

# MACD (Moving Average Convergence Divergence)
# Meaning: Shows momentum changes and trend strength.
# Bullish: MACD crosses above signal line.
# Bearish: MACD crosses below signal line.
def calculate_MACD(df, fast=12, slow=26, signal=9):
    pass  # Implement calculation here

# Bollinger Bands (20 days)
# Meaning: Measures volatility and extremes.
# Bullish: Price moves upward from lower band.
# Bearish: Price retreats downward from upper band.
def calculate_bollinger_bands(df, window=20):
    pass  # Implement calculation here

# ADX (Average Directional Index)
# Meaning: Measures trend strength (above 25 is significant).
# Bullish: ADX >25 with rising price.
# Bearish: ADX >25 with falling price.
def calculate_ADX(df, window=14):
    pass  # Implement calculation here

# OBV (On-Balance Volume, 30-60 days)
# Meaning: Shows buying/selling pressure.
# Bullish: OBV rising with rising price.
# Bearish: OBV falling with falling price.
def calculate_OBV(df):
    pass  # Implement calculation here

# =============================================
# Long-Term Indicators (Months to Years)
# =============================================

# 200-Day Moving Average
# Meaning: Indicates long-term trend direction.
# Bullish: Price above 200-day MA.
# Bearish: Price below 200-day MA.
def calculate_long_term_MA(df, window=200):
    pass  # Implement calculation here

# Golden Cross / Death Cross (50-day and 200-day MA)
# Meaning: Signals major shifts in long-term trend.
# Bullish: 50-day MA crosses above 200-day MA (Golden Cross).
# Bearish: 50-day MA crosses below 200-day MA (Death Cross).
def calculate_MA_crossover(df, short_window=50, long_window=200):
    pass  # Implement calculation here

# Accumulation/Distribution Line (A/D)
# Meaning: Tracks institutional buying or selling pressure.
# Bullish: Rising A/D line suggests institutional accumulation.
# Bearish: Falling A/D line suggests institutional selling.
def calculate_AD_line(df):
    pass  # Implement calculation here

# Fundamental Ratios (P/E Ratio, etc.)
# Meaning: Evaluates stock valuation based on earnings.
# Bullish: Stable or declining P/E, undervaluation.
# Bearish: High or rising P/E, possible overvaluation.
def get_fundamental_ratios(ticker):
    pass  # Implement retrieval here

# Medium term

# Long term

def main():
    # Inputs
    ticker = "MSFT"
    cmpy = yf.Ticker(ticker)

    start_date_input = input('Enter start date (YYYY-MM-DD): ')
    end_date_input = input('Enter end date (YYYY-MM-DD): ')

    start_date = date.fromisoformat(start_date_input) if start_date_input else None
    end_date = date.fromisoformat(end_date_input) if end_date_input else None

    df = cmpy.history(start=start_date, end=end_date)
    print(df.head())


# Plot key metrics
if __name__ == "__main__":
    main()

