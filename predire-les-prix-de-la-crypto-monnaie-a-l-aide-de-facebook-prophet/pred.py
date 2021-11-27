import streamlit as st
import yfinance as yf
import streamlit as st
import datetime as dt
from plotly import graph_objs as go


def app():
    # Détermination des dates
    @st.cache
    def load_data(df1):
        return df1

    start1 = dt.datetime.today() - dt.timedelta(2 * 365)
    end1 = dt.datetime.today()

    start = st.sidebar.date_input('Date de début', start1)

    end = st.sidebar.date_input('Date de fin', end1)

    # Importation des données
    df_btc = yf.download("BTC-USD", start=start, end=end, group_by="ticker")
    df_bnb = yf.download("BNB-USD", start=start, end=end, group_by="ticker")
    df_sol = yf.download("SOL1-USD", start=start, end=end, group_by="ticker")
    df_usdt = yf.download("USDT-USD", start=start, end=end, group_by="ticker")
    df_eth = yf.download("ETH-EUR", start=start, end=end, group_by="ticker")
    df_ada = yf.download("ADA-EUR", start=start, end=end, group_by="ticker")

    # Sidebar
    choice2 = ["BTC", "BNB", "SOL", "USDT", "ETH", "ADA"]
    ticker3 = st.sidebar.selectbox("Sélectionnez un bitcoin ...", choice2)
    ticker1 = st.sidebar.selectbox(
        'Choisir une valeur',
        df_bnb.columns)

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

    # Affichage BNB
    if ticker3 == "BNB":
        st.header("BNB-USD")
        df = load_data(df_bnb[ticker1])
        st.write(df.head())

    # Affichage BTC
    if  ticker3 == "BTC":
        st.header("BTC-USD")
        df = load_data(df_btc[ticker1])
        st.write(df.head())

    # Affichage SOL
    if  ticker3 == "SOL":
        st.header("SOL1-USD")
        df = load_data(df_sol[ticker1])
        st.write(df.head())

    # Affichage USDT
    if ticker3 == "USDT":
        st.header("USDT-USD")
        df = load_data(df_usdt[ticker1])
        st.write(df.head())

    # Affichage ETH
    if ticker3 == "ETH":
        st.header("ETH")
        df = load_data(df_eth[ticker1])
        st.write(df.head())

    # Affichage ADA
    if ticker3 == "ADA":
        st.header("ADA-EUR")
        df = load_data(df_ada[ticker1])
        st.write(df.head())




    # Prédiction
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