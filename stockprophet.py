import pandas as pd
from fbprophet import Prophet
import streamlit as st

st.title('株価の時系列予測')

st.subheader('株価データの読み込み(6758:Sony)')
df = pd.read_csv("/Users/io/Desktop/prophet/stockdata/6758_2015_2020.csv", encoding = 'utf-8', names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'], skiprows=[0, 1])

st.write(df)

df = df.loc[:,['Date','Adj Close']]

df = df.rename(columns={'Date':'ds', 'Adj Close':'y'})

m = Prophet()

m.fit(df)

future = m.make_future_dataframe(periods=250)
future = future[future['ds'].dt.weekday < 5]

forecast = m.predict(future)

fig1 = m.plot(forecast)

st.header('予測結果')
st.write(fig1)

fig2 = m.plot_components(forecast)
st.header('周期性')
st.write(fig2)