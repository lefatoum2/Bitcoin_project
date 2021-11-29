import yfinance as yf
import streamlit as st
import datetime as dt


# Détermination des dates
start1 = dt.datetime.today() - dt.timedelta(2 * 365)
end1 = dt.datetime.today()
start = st.sidebar.date_input('Date de début', start1)
end = st.sidebar.date_input('Date de fin', end1)

choice2 = ["EUR", "USD"]
ticker2 = st.sidebar.selectbox('Choisir une monnaie..', choice2)
choice3 = [f"BTC-{ticker2}", f"BNB-{ticker2}", f"SOL1-{ticker2}", f"USDT-{ticker2}", f"ETH-{ticker2}", f"ADA-{ticker2}"]
ticker3 = st.sidebar.multiselect("Sélectionnez un bitcoin ...", choice3)

metric = 'Close'
colnames = []
if ticker2:
    first = True
    for ticker in ticker3:
        data = yf.download(ticker, start=start, end=end, group_by="ticker")
        if first:
            metric = st.sidebar.selectbox('Choisir la valeur..', data.columns)
            combined = data[[metric]].copy()
            colnames.append(ticker)
            combined.columns = colnames
            first = False
        else:
            combined = combined.join(data[metric])
            colnames.append(ticker)
            combined.columns = colnames

st.line_chart(combined,use_container_width=True)
