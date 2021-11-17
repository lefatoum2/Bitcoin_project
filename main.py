# import streamlit-heroku as sth
import yfinance as yf
import streamlit as st
from PIL import Image


# Titre et image
st.title("Down Jones")
image = Image.open('./bitcoin.jpeg')
st.markdown("BITCOIN, l'or numérique")
st.image(image)
