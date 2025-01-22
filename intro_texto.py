import streamlit as st
import datetime

def imprime_estado():
    print(st.session_state)

st.session_state.texto_corto = st.text_input("Introduce un texto", 
                                             max_chars=60, 
                                             on_change = imprime_estado)

st.session_state.texto_largo = st.text_area("Introduce un texto largo", 
                                      on_change = imprime_estado)


st.session_state.numero_entero = st.number_input('Introduce un número', 
                                                min_value=10, 
                                                max_value=100, 
                                                on_change = imprime_estado)


st.session_state.fecha = st.date_input("Introduce una fecha", 
                                      on_change = imprime_estado)

# Permitir elegir dentro de un rango dado
today = datetime.date.today()
last_week = today - datetime.timedelta(days=7)

st.session_state.rango_fechas = st.date_input("Selecciona el rango de fechas ",
    value = (last_week ,today),
    min_value = datetime.date(2012, 12, 1),
    max_value = datetime.date.today(), format="MM.DD.YYYY", 
                                      on_change = imprime_estado)

st.session_state.hora = st.time_input("Introduce una hora", step = datetime.timedelta(minutes=5), 
                                      on_change = imprime_estado)

st.json(st.session_state)
