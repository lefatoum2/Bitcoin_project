import streamlit as st
import acceuil
import graph
import pred
#import twitt.twit as twit
import reddit1
import corre

# Title of the Application
st.markdown("Christian MBARGA, Julien SISAVATH, Valentin VERMES")

# Choice of page
# page_choices = {"Home": acceuil, "Graphes": graph, "Twitter": twit, "Reddit": reddit1, "Corrélations":corre, "Prédictions": pred}
page_choices = {"Home": acceuil, "Graphes": graph, "Reddit": reddit1, "Corrélations":corre, "Prédictions": pred}

# Create radio button for the page choice
page_selection = st.sidebar.selectbox("Selectionnez une page", list(page_choices.keys()))

# Choosing the page based on the user selection from radio button
page = page_choices[page_selection]

# Display the page
with st.spinner(f'Chargement {page_selection} ...'):
    page.app()
