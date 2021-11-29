import streamlit as st
from PIL import Image


def app():
    # Image
    image1 = Image.open('./bitcoin.jpeg')

    #st.set_page_config(page_title="BITCOIN, l'or numérique", page_icon=image1, layout='wide',
    #                   initial_sidebar_state="auto")

    # Titre
    st.title("BITCOIN, l'or numérique")

    # Affichage Image Bitcoin
    st.image(image1, use_column_width=True)
    st.markdown('<style>body{background-color: lightblue ;}</style>', unsafe_allow_html=True)

