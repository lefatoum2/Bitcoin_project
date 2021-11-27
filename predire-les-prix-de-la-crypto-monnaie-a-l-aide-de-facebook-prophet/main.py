# Data

import streamlit as st
from cryptocmd import CmcScraper

### Select ticker
selected_ticker = st.sidebar.text_input("Select a ticker for prediction (i.e. BTC, ETH, LINK, etc.)", "BTC")


### Initialise scraper
@st.cache
def load_data(selected_ticker):
    init_scraper = CmcScraper(selected_ticker)
    df = init_scraper.get_dataframe()
    return df


### Load the data
data_load_state = st.sidebar.text('Loading data...')
df = load_data(selected_ticker)
data_load_state.text('Loading data... done!')




# Graphiques

import streamlit as st
from cryptocmd import CmcScraper
from plotly import graph_objs as go

### Get the scraped data
data = scraper.get_dataframe()

### Create overview of the latest rows of data
st.subheader('Raw data')
st.write(data.head())


### Plot functions for regular & log plots
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


def plot_raw_data_log():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="Close"))
    fig.update_yaxes(type="log")
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


### Create checkbox for plotting (log) data
plot_log = st.checkbox("Plot log scale")
if plot_log:
    plot_raw_data_log()
else:
    plot_raw_data()


# Prédictions

import streamlit as st
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

### Use button to start model prediction
if st.button("Predict"):

    ### Get the required data & rename the columns so fbprophet can read it
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    ### Create Prophet model
    m = Prophet(
        changepoint_range=0.8,  # percentage of dataset to train on
        yearly_seasonality='auto',  # taking yearly seasonality into account
        weekly_seasonality='auto',  # taking weekly seasonality into account
        daily_seasonality=False,  # taking daily seasonality into account
        seasonality_mode='multiplicative'
        # additive (for more linear data) or multiplicative seasonality (for more non-linear data)
    )

    m.fit(df_train)

    ### Predict using the model
    future = m.make_future_dataframe(periods=365)
    forecast = m.predict(future)

    ### Show and plot forecast
    st.subheader('Forecast data')
    st.write(forecast.head())

    st.subheader(f'Forecast plot for 365 days')
    fig1 = plot_plotly(m, forecast)
    if plot_log:
        fig1.update_yaxes(type="log")
    st.plotly_chart(fig1)

    st.subheader("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)