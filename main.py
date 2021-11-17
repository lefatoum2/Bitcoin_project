# import streamlit-heroku as sth
import yfinance as yf
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
import datetime as dt

# Titre et image
st.title("BITCOIN, l'or numérique")
image1 = Image.open('./bitcoin.jpeg')
# st.markdown(" l'or numérique")
#st.image(image1)

start = dt.datetime(2018, 5, 31)
#end = dt.datetime(2021, 1, 30)
end = dt.datetime.now()



st.markdown(" ## BTC")
st.markdown("## SOL")
st.markdown("## USDT")
st.markdown("## ETH")
st.markdown("## BNB")
st.markdown("## COVID-19")