import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta
import re
import streamlit as st

# Decorator function
def safe_copy(func):
    def wrapper(df, *args, **kwargs):
        return func(df.copy(), *args, **kwargs)
    return wrapper


# Calculate required time frame
def timeframe_default(start_date='', end_date=''):
    if start_date == '':
        start_date = date.today() - relativedelta(years=10)
    else:
        date.fromisoformat(start_date)

    if end_date == '':
        end_date = date.today()
    else:
        date.fromisoformat(start_date)

    return start_date, end_date


# =============================================
# Short-Term Indicators (Days to Weeks)
# =============================================

# RSI (Relative Strength Index)
# Meaning: Measures if stock is overbought (>70) or oversold (<30).
# Bullish: RSI moves above 30 (from oversold).
# Bearish: RSI moves below 70 (from overbought).
@safe_copy
def calculate_short_term_RSI(df, col='Close', window=14):
    # Calculate difference in price between each day
    delta = df[col].diff()
    # Calculate the gains and losses in ABSOLUTE terms
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain/loss
    rsi = 100 - (100 / (1 + rs))
    df[f'RSI_{window}days'] = rsi
    return df

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
@safe_copy
def calculate_short_term_MA(df, col='Close', window=10):
    sma = df[col].rolling(window=window).mean()
    df[f'SMA_{window}days'] = sma
    return df

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
def calculate_long_term_MA(df, col='Close', window=200):
    lma = df[col].rolling(window=window).mean()
    df[f'LMA_{window}days'] = lma
    return df

# Golden Cross / Death Cross (50-day and 200-day MA)
# Meaning: Signals major shifts in long-term trend.
# Bullish: 50-day MA crosses above 200-day MA (Golden Cross).
# Bearish: 50-day MA crosses below 200-day MA (Death Cross).
def calculate_MA_crossover(df, short_window=50, long_window=200):
    # Find out if moving averages are present in df
    short_col = f'SMA_{short_window}days'
    long_col = f'LMA_{long_window}days'

    if short_col not in df.columns:
        df = calculate_short_term_MA(df, window=short_window)

    if long_col not in df.columns:
        df = calculate_long_term_MA(df, window=long_window)

    # Crossover logic
    df[f'MA Crossover ({short_window} vs {long_window})'] = 0

    # Bull = 1 (Golden Cross); Bear = -1 (Death Cross)
    df.loc[
        (df[short_col] > df[long_col]) & (df[short_col].shift(1) <= df[long_col].shift(1)),
        f'MA Crossover ({short_window} vs {long_window})'] = 1
    df.loc[
        (df[short_col] < df[long_col]) & (df[short_col].shift(1) >= df[long_col].shift(1)),
        f'MA Crossover ({short_window} vs {long_window})'] = -1
    return df

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

# Chain populate indicators
def add_technical_indicators(df, short_window=50, long_window=200):
    return(
        df
        # Short term indicators
        .pipe(calculate_short_term_RSI, col='Close', window=14)
        .pipe(calculate_short_term_MA, col='Close', window=short_window)
        # Medium term indicators
        # Long term indicators
        .pipe(calculate_long_term_MA, col='Close', window=long_window)
        .pipe(calculate_MA_crossover, short_window=short_window, long_window=long_window)
    )


def main():
    # Inputs
    ticker = "MSFT"
    cmpy = yf.Ticker(ticker)

    start_date_input = input('Enter start date (YYYY-MM-DD): ')
    end_date_input = input('Enter end date (YYYY-MM-DD): ')

    start_date, end_date = timeframe_default(start_date=start_date_input, end_date=end_date_input)

    df = cmpy.history(start=start_date, end=end_date)
    # print(df.head())

    # Generate indicators
    df_with_indicators = add_technical_indicators(df)
    # Clean up NaN values @@@
    print(f'\nNew df:\n {df_with_indicators.tail()}')

# Plot key metrics
if __name__ == "__main__":
    main()

