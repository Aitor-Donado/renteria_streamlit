import streamlit as st
import pandas as pd

st.title("Datos heart_data.csv")

data = pd.read_csv("Ejemplo_visualizaciones/heart_data.csv")

st.dataframe(data)