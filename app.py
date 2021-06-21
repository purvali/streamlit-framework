#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np
import streamlit as st
import datetime as dt
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
import json


# In[2]:


st.set_page_config(page_title="Market Profile Chart (US S&P 500)",layout="wide")
st.title('Market Profile Chart S&P 500 - TDI milestone project')
st.header('An interactive chart of stock closing prices using Streamlit and Plot.ly.')
#ticker = st.sidebar.selectbox('Choose a S&P 500 Stock')
# Choose time interval 
ticker = st.sidebar.text_input('Ticker e.g AAPL', value='AAPL')
#i = st.sidebar.selectbox('Year', ('2017', '2018', '2019','2020'))
#j = st.sidebar.selectbox('Month', ('Jan','Feb','March','April', 'May','June','July','August', 'Sept','Oct', 'Nov', 'Dec'))

#i = st.sidebar.selectbox("Interval in minutes",("1m", "5m", "15m", "30m"))st.sidebar.selectbox('Year', ('2017', '2018', '2019','2020'))


# In[3]:


# Processing of Stock ticker and data

# get data on this ticker
#ticker = 'AAPL'
stock = yf.Ticker(ticker)
print(type(stock))
# get historical prices
history_df = stock.history(period = '1mo', start='2020-01-01', end='2020-12-01')
#prices = history_data['Close']
#volumes = history_data['Volume']
st.write("""## Stock Price Jan 2020 to Dec 2020""")
#st.line_chart(history_df.Close)
#st.line_chart(history_df.Volume)
print(type(history_df))
history_df.head()


# In[4]:


#history_df['Date'] = history_df.index.strptime("%d-%m-%Y")
#history_df = history_df.set_index(pd.DatetimeIndex(history_df['Date'].values))


history_df.reset_index(inplace=True)
fig = go.Figure(
    data=[
      go.Candlestick(
           x=history_df["Date"],
           open=history_df["Open"],           
           high=history_df["High"],
           low=history_df["Low"],
           close=history_df["Close"],
        )
    ]
 )
st.plotly_chart(fig)
