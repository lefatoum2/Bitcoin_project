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
choice1 = ["BTC", "BNB", "SOL1", "USDT", "ETH", "ADA"]
choice2 = ["EUR", "USD"]
st.sidebar.header("Premier Graphe")
ticker1 = st.sidebar.selectbox('Choisir une valeur bitcoin',choice1)
ticker2 = st.sidebar.selectbox('Choisir une monnaie..',choice2)
#ticker3 = st.sidebar.multiselect("Sélectionnez un bitcoin ...",choice1)

if ticker1 and ticker2:
    df = yf.download(f"{ticker1}-{ticker2}", start=start, end=end, group_by="ticker")
    ticker3 = st.sidebar.selectbox(
        'Choisir une valeur',
        df.columns)
    st.header(f"{ticker1}-{ticker2}")
    if ticker3:
        st.line_chart(df[ticker3])
        st.sidebar.header("Second Graphe")
        ticker4 = st.sidebar.selectbox('Choisir une deuxième valeur bitcoin', choice1)
        ticker5 = st.sidebar.selectbox('Choisir une seconde monnaie..', choice2)
        if ticker4 and ticker5:
            df2 = yf.download(f"{ticker4}-{ticker5}", start=start, end=end, group_by="ticker")
            st.header(f"{ticker4}-{ticker5}")
            st.line_chart(df2[ticker3])

#ticker3 = st.sidebar.multiselect("Sélectionnez un bitcoin ...", choice2)
