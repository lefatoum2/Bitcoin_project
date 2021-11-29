import yfinance as yf
import streamlit as st
import datetime as dt
import pandas as pd
import requests
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt

# Détermination des dates
start1 = dt.datetime.today() - dt.timedelta(2 * 365)
end1 = dt.datetime.today()

start = st.sidebar.date_input('Date de début', start1)

end = st.sidebar.date_input('Date de fin', end1)

# Sidebar
choice1 = ["BTC", "BNB", "SOL1", "USDT", "ETH", "ADA"]
choice2 = ["EUR", "USD"]
ticker2 = st.sidebar.selectbox('Choisir une monnaie..', choice2)


choice3 = [f"BTC-{ticker2}", f"BNB-{ticker2}", f"SOL1-{ticker2}", f"USDT-{ticker2}", f"ETH-{ticker2}", f"ADA-{ticker2}"]
colnames = []
first = True
for ticker in choice3:
    data = yf.download(ticker, start=start, end=end, group_by="ticker")

    if first:
        ticker3 = st.sidebar.selectbox('Choisir une valeur', data.columns)
        combined = data[[ticker3]].copy()
        colnames.append(ticker)
        combined.columns = colnames
        first = False
    else:
        combined = combined.join(data[ticker3])
        colnames.append(ticker)
        combined.columns = colnames

st.title('Corrélation')
fig3 = plt.figure()
sns.heatmap(combined.corr())
st.pyplot(fig3)
