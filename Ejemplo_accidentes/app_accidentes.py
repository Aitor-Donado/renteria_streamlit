import streamlit as st
import pandas as pd

st.title("Datos Accidentes Euskadi")
df = pd.read_csv("Ejemplo_accidentes/accidentes_2022.csv")
df.drop(columns=["Unnamed: 0", "incidenceType", "sourceId", "autonomousRegion", "endDate", "incidenceName", "carRegistration", "pkEnd"], inplace=True)
df.rename(columns={"pkStart": "pk"}, inplace=True)

st.table(df.head(20))

col1, col2 = st.columns(2)


with col1:
    grafico_causa = df["cause"].value_counts().plot(kind="pie")
    st.pyplot(grafico_causa.figure)
    grafico_ciudad = df["cityTown"].value_counts().plot(kind="pie")
    st.pyplot(grafico_ciudad.figure)

df2 = df[["incidenceId", "latitude", "longitude"]]

import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
# Crear el mapa centrado en una ubicación específica del coordenadas del País Vasco
mapa_accidentes_heat = folium.Map(location=[43, -2.6], zoom_start=8)

# Crear una lista de coordenadas (latitud, longitud) para los accidentes
coordenadas_accidentes = df2[['latitude', 'longitude']].dropna().values.tolist()

# Añadir las ubicaciones de los accidentes al mapa con marcadores de calor
HeatMap(coordenadas_accidentes).add_to(mapa_accidentes_heat)

# Mostrar el mapa
with col2:
    st.markdown("### Mapa de calor")
    st_data = st_folium(mapa_accidentes_heat, width=350)

st.divider()

st.markdown("### Mapa con puntos aglomerables")
from folium.plugins import MarkerCluster

# Crear el mapa centrado en una ubicación específica del coordenadas del País Vasco
mapa_accidentes = folium.Map(location=[43, -2.6], zoom_start=9.5)

# Crear una lista de coordenadas (latitud, longitud) para los accidentes
coordenadas_accidentes = df2[['latitude', 'longitude']].dropna().values.tolist()

# Añadir las ubicaciones de los accidentes al mapa con marcadores de calor
MarkerCluster(coordenadas_accidentes).add_to(mapa_accidentes)

# Mostrar el mapa
with st.expander("Ver mapa"):
    st_data = st_folium(mapa_accidentes, width=725)