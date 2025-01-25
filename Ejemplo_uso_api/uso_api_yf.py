import streamlit as st
# pip install yfinance
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Visualización de un DataFrame
df = pd.read_csv("Empresas.csv")
df = df.drop("Unnamed: 0", axis=1)
st.dataframe(df)

# Es un selector desplegable que sólo permite una elección
opciones = df["empresa"]
select = st.selectbox("Elige una empresa", options= opciones)
if select:
    ticker = df[df["empresa"]==select]["ticker.yf"].values[0]
    st.write(ticker)
    empresa = yf.Ticker(ticker)
    hist_empresa = empresa.history(period="max")
    #st.table(hist_empresa)

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

    fig = go.Figure(data=[go.Candlestick(x=hist_empresa.index,
                    open=hist_empresa['Open'],
                    high=hist_empresa['High'],
                    low=hist_empresa['Low'],
                    close=hist_empresa['Close'])])

    #fig.show()
    st.plotly_chart(fig)

