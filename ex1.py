import yfinance as yf
import streamlit as st
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
import datetime as dt

image1 = Image.open('./bitcoin.jpeg')
st.set_page_config(page_title="BITCOIN", page_icon=image1, layout='centered', initial_sidebar_state="auto",
                   menu_items=None)


col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")


with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")