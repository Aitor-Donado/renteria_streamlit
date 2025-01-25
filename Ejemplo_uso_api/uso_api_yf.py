import streamlit as st
# pip install yfinance
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd

# Visualización de un DataFrame
df = pd.read_csv("Empresas.csv")
df = df.drop("Unnamed: 0", axis=1)
st.dataframe(df)

col1, col2 = st.columns(2)

with col1:
    # Es un selector desplegable que sólo permite una elección
    mercados = df["mercado"].unique()
    mercado_elegido = st.selectbox("Elige un mercado", options= mercados)

with col2:
    # Es un selector desplegable que sólo permite una elección
    if mercado_elegido:
        df = df[df["mercado"]==mercado_elegido]
    opciones = df["empresa"]
    select = st.selectbox("Elige una empresa", options= opciones)
if select:
    ticker = df[df["empresa"]==select]["ticker.yf"].values[0]
    st.write(ticker)
    empresa = yf.Ticker(ticker)
    hist_empresa = empresa.history(period="max")
    #st.table(hist_empresa)

    fig = go.Figure(data=[go.Candlestick(x=hist_empresa.index,
                    open=hist_empresa['Open'],
                    high=hist_empresa['High'],
                    low=hist_empresa['Low'],
                    close=hist_empresa['Close'])])

    #fig.show()
    st.plotly_chart(fig)

