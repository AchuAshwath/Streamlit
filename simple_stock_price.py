import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple stock market Price app

Shown are the stock **closing price**,*volume**,**high price** and **low price** of google

""")
# define ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get historical prices
tickerDf = tickerData.history(period='1d', start='2000-5-14', end='2021-4-12')

st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume price
""")
st.line_chart(tickerDf.Volume)
st.write("""
## High price
""")
st.line_chart(tickerDf.High)
st.write("""
## Low price
""")
st.line_chart(tickerDf.Low)