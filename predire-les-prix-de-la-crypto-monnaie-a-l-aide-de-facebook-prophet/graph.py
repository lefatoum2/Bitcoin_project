import yfinance as yf
import streamlit as st
import datetime as dt
import pandas as pd
import requests
from PIL import Image


def app():
    # Détermination des dates
    start1 = dt.datetime.today() - dt.timedelta(2 * 365)
    end1 = dt.datetime.today()

    start = st.sidebar.date_input('Date de début', start1)

    end = st.sidebar.date_input('Date de fin', end1)

    # Importation des données
    df_btc = yf.download("BTC-USD", start=start, end=end, group_by="ticker")
    df_bnb = yf.download("BNB-USD", start=start, end=end, group_by="ticker")
    df_sol = yf.download("SOL1-USD", start=start, end=end, group_by="ticker")
    df_usdt = yf.download("USDT-USD", start=start, end=end, group_by="ticker")
    df_eth = yf.download("ETH-EUR", start=start, end=end, group_by="ticker")
    df_ada = yf.download("ADA-EUR", start=start, end=end, group_by="ticker")

    # Sidebar
    choice2 = ["BTC", "BNB", "SOL", "USDT", "ETH", "ADA"]
    ticker3 = st.sidebar.multiselect("Sélectionnez un bitcoin ...",choice2)
    ticker1 = st.sidebar.selectbox(
        'Choisir une valeur',
        df_bnb.columns)
    ticker4 = ["EUR", "USD"]


# Affichage BNB
    if "BNB" in ticker3:
        st.header("BNB-USD")
        st.line_chart(df_bnb[ticker1])

    # Affichage BTC
    if "BTC" in ticker3:
        st.header("BTC-USD")
        st.line_chart(df_btc[ticker1])


    # Affichage SOL
    if "SOL" in ticker3:
        st.header("SOL1-USD")
        st.line_chart(df_sol[ticker1])

    # Affichage USDT
    if "USDT" in ticker3:
        st.header("USDT-USD")
        st.line_chart(df_usdt[ticker1])


    # Affichage ETH
    if "ETH" in ticker3:
        st.header("ETH-EUR")
        st.line_chart(df_eth[ticker1])

    # Affichage ADA
    if "ADA" in ticker3:
        st.header("ADA-EUR")
        st.line_chart(df_ada[ticker1])


