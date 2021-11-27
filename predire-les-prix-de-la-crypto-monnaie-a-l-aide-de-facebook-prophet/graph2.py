import yfinance as yf
import streamlit as st
import datetime as dt
import pandas as pd
import requests
from PIL import Image

# Détermination des dates
start1 = dt.datetime.today() - dt.timedelta(2 * 365)
end1 = dt.datetime.today()

start = st.sidebar.date_input('Date de début', start1)

end = st.sidebar.date_input('Date de fin', end1)


# Sidebar
choice1 = ["BTC", "BNB", "SOL", "USDT", "ETH", "ADA"]
choice2 = ["EUR", "USD"]
ticker1 = st.sidebar.selectbox('Choisir une valeur bitcoin',choice1)
ticker2 = st.sidebar.selectbox('Choisir une monnaie..',choice2)
#ticker3 = st.sidebar.multiselect("Sélectionnez un bitcoin ...",choice1)

if ticker1 and ticker2:
    df = yf.download(f"{ticker1}-{ticker2}", start=start, end=end, group_by="ticker")
    ticker4 = st.sidebar.selectbox(
        'Choisir une valeur',
        df.columns)
    st.header(f"{ticker1}-{ticker2}")
    if ticker4:
        st.line_chart(df[ticker4])

#ticker3 = st.sidebar.multiselect("Sélectionnez un bitcoin ...", choice2)
