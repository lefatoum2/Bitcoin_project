# pip install streamlit fbprophet yfinance plotly
import streamlit as st
import datetime as dt
import yfinance as yf
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

START = dt.datetime.today() - dt.timedelta(2 * 365)
TODAY = dt.datetime.today()

st.title('Prédiction de bitcoin')
# Sidebar
choice1 = ["BTC", "BNB", "SOL1", "USDT", "ETH", "ADA"]
choice2 = ["EUR", "USD"]
ticker2 = st.sidebar.selectbox('Choisir une monnaie..', choice2)
choice3 = [f"BTC-{ticker2}", f"BNB-{ticker2}", f"SOL1-{ticker2}", f"USDT-{ticker2}", f"ETH-{ticker2}", f"ADA-{ticker2}"]
if ticker2:
    selected_stock = st.selectbox('Select dataset for prediction', choice3)


period = int(st.sidebar.number_input('Nombre de jours de prédiction:', min_value=0, max_value=1000000, value=365, step=1))


@st.cache
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text('Chargement data...')
data = load_data(selected_stock)
data_load_state.text('Data... chargé!')

st.subheader('Raw data')
st.write(data.tail())


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Prédiction data')
st.write(forecast.tail())

st.write(f'Prédictions pour les {period} jours')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)