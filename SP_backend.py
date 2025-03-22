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


# Calculate necessary metrics


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

