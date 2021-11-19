import yfinance as yf
import streamlit as st
import datetime as dt
# import talib
import ta
import pandas as pd
import requests
# yf.pdr_override()
from PIL import Image


# Image
image1 = Image.open('./bitcoin.jpeg')

st.set_page_config(page_title="BITCOIN, l'or numérique", page_icon=image1, layout='wide', initial_sidebar_state="auto")

# Titre
st.title("BITCOIN, l'or numérique")

# Affichage Image Bitcoin
st.image(image1, use_column_width= True)
st.markdown('<style>body{background-color: lightblue ;}</style>',unsafe_allow_html= True)

# Détermination des dates
start1 = dt.datetime.today() - dt.timedelta(2 * 365)
end1 = dt.datetime.today()

start = st.sidebar.date_input('start date', start1)

end = st.sidebar.date_input('end date', end1)

# Importation des données
df_btc = yf.download("BTC-USD", start=start, end=end, group_by="ticker")
df_bnb = yf.download("BNB-USD", start=start, end=end, group_by="ticker")
df_sol = yf.download("SOL1-USD", start=start, end=end, group_by="ticker")
df_usdt = yf.download("USDT-USD", start=start, end=end, group_by="ticker")
df_eth = yf.download("ETH-EUR", start=start, end=end, group_by="ticker")
df_ada = yf.download("ADA-EUR", start=start, end=end, group_by="ticker")


# Sidebar
ticker1 = st.sidebar.selectbox(
    'Choisir une valeur',
    df_bnb.columns)



col1, col2 = st.columns(2)
# Affichage BNB
with col1:
    st.header("BNB")
    st.line_chart(df_bnb[ticker1])

# Affichage BTC
with col2:
    st.header("BTC")
    st.line_chart(df_btc[ticker1])

col3, col4 = st.columns(2)
# Affichage SOL
with col3:
    st.header("SOL")
    st.line_chart(df_sol[ticker1])

# Affichage USDT
with col4:
    st.header("USDT-USD")
    st.line_chart(df_usdt[ticker1])

col5, col6 = st.columns(2)
# Affichage ETH
with col5:
    st.header("ETH")
    st.line_chart(df_eth[ticker1])

# Affichage ADA
with col6:
    st.header("ADA")
    st.line_chart(df_ada[ticker1])

# Affichage Covid-19
st.markdown("## COVID-19")
# st.line_chart(data['Adj Close'])