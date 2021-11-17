# import streamlit-heroku as sth
import yfinance as yf
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
import datetime as dt

# Image
image1 = Image.open('./bitcoin.jpeg')

st.set_page_config(page_title="BITCOIN, l'or numérique", page_icon=image1, layout='wide', initial_sidebar_state="auto",
                   menu_items=None)
# Titre
st.title("BITCOIN, l'or numérique")

# Affichage Image Bitcoin
st.image(image1)

# Détermination des dates
start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

# Importation des données
df_btc = yf.download("BTC-USD", start=start, end=end, group_by="ticker")
df_bnb = yf.download("BNB-USD", start=start, end=end, group_by="ticker")
df_sol = yf.download("SOL1-USD", start=start, end=end, group_by="ticker")
df_usdt = yf.download("USDT-USD", start=start, end=end, group_by="ticker")
df_eth = yf.download("ETH-EUR", start=start, end=end, group_by="ticker")

# Sidebar
ticker1 = st.sidebar.selectbox(
    'Choisir une valeur',
    df_btc.columns)

date1 = st.sidebar.date_input('start date', dt.date(2018, 1, 1))

date2 = st.sidebar.date_input('end date', dt.date(2021, 1, 1))

col1, col2 = st.columns(2)

# Affichage BNB
with col1:
    st.header("BNB")
    fig = go.Figure(data=go.Scatter(x=df_bnb.loc[start:end], y=df_bnb[ticker1]))
    fig.update_layout(
        title={
            'text': "BNB",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

# Affichage BTC
with col2:
    st.header("BTC")
    fig = go.Figure(data=go.Scatter(x=df_btc.loc[start:end], y=df_bnb[ticker1]))
    fig.update_layout(
        title={
            'text': "BTC",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

col3, col4, col5 = st.columns(3)

# Affichage SOL
with col3:
    st.header("SOL")
    fig = go.Figure(data=go.Scatter(x=df_sol.loc[start:end], y=df_bnb[ticker1]))
    fig.update_layout(
        title={
            'text': "SOL",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

# Affichage USDT
with col4:
    st.header("USDT-USD")
    fig = go.Figure(data=go.Scatter(x=df_usdt.loc[start:end], y=df_bnb[ticker1]))
    fig.update_layout(
        title={
            'text': "USDT-USD",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

# Affichage ETH
with col5:
    st.header("ETH")
    fig = go.Figure(data=go.Scatter(x=df_eth.loc[start:end], y=df_bnb[ticker1]))
    fig.update_layout(
        title={
            'text': "ETH",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig, use_container_width=True)

# Affichage Covid-19
st.markdown("## COVID-19")
fig = go.Figure(data=go.Scatter())
fig.update_layout(
    title={
        'text': "COVID-19",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig, use_container_width=True)