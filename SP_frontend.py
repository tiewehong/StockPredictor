import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

st.title("Interactive Stock Analysis - Commonwealth Bank (CBA)")

# User inputs:
ticker = st.sidebar.text_input("Ticker", value='CBA.AX')
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime('2020-01-01'))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime('today'))

# Fetch data
data = yf.download(ticker, start=start_date, end=end_date)

# Plotting interactive plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Close Price'))
fig.update_layout(title=f'{ticker} Close Price', xaxis_title='Date', yaxis_title='Price AUD')

st.plotly_chart(fig, use_container_width=True)
