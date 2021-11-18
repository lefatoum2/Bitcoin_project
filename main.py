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
start1 = dt.datetime.today() - dt.timedelta(2 * 365)
end1 = dt.datetime.today()

# Importation des données
df_btc = yf.download("BTC-USD", start=start1, end=end1, group_by="ticker")
df_bnb = yf.download("BNB-USD", start=start1, end=end1, group_by="ticker")
df_sol = yf.download("SOL1-USD", start=start1, end=end1, group_by="ticker")
df_usdt = yf.download("USDT-USD", start=start1, end=end1, group_by="ticker")
df_eth = yf.download("ETH-EUR", start=start1, end=end1, group_by="ticker")
df_ada = yf.download("ADA-EUR", start=start1, end=end1, group_by="ticker")

# df_btc = df_btc.reset_index()
# df_bnb = df_bnb.reset_index()
# df_sol = df_sol.reset_index()
# df_usdt = df_usdt.reset_index()
# df_eth = df_eth.reset_index()
# df_ada = df_ada.reset_index()

# Sidebar
ticker1 = st.sidebar.selectbox(
    'Choisir une valeur',
    df_bnb.columns)

start = st.sidebar.date_input('start date', start1)

end = st.sidebar.date_input('end date', end1)

col1, col2 = st.columns(2)
# Affichage BNB
with col1:
    st.header("BNB")
    fig1 = go.Figure(data=go.Scatter(y=df_bnb[ticker1]))
    fig1.update_layout(
        title={
            'text': "BNB",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig1, use_container_width=True)

# Affichage BTC
with col2:
    st.header("BTC")
    fig2 = go.Figure(data=go.Scatter(y=df_bnb[ticker1]))
    fig2.update_layout(
        title={
            'text': "BTC",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)
# Affichage SOL
with col3:
    st.header("SOL")
    fig3 = go.Figure(data=go.Scatter(y=df_bnb[ticker1]))
    fig3.update_layout(
        title={
            'text': "SOL",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig3, use_container_width=True)

# Affichage USDT
with col4:
    st.header("USDT-USD")
    fig4 = go.Figure(data=go.Scatter(y=df_bnb[ticker1]))
    fig4.update_layout(
        title={
            'text': "USDT-USD",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig4, use_container_width=True)

col5, col6 = st.columns(2)
# Affichage ETH
with col5:
    st.header("ETH")
    fig5 = go.Figure(data=go.Scatter(y=df_bnb[ticker1]))
    fig5.update_layout(
        title={
            'text': "ETH",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig5, use_container_width=True)

# Affichage ADA
with col6:
    st.header("ADA")
    fig6 = go.Figure(data=go.Scatter(y=df_bnb[ticker1]))
    fig6.update_layout(
        title={
            'text': "ADA",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig6, use_container_width=True)

# Affichage Covid-19
st.markdown("## COVID-19")
fig7 = go.Figure(data=go.Scatter())
fig7.update_layout(
    title={
        'text': "COVID-19",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'})
st.plotly_chart(fig7, use_container_width=True)