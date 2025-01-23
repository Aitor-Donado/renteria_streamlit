import streamlit as st
from conversor import convertir_presion

# Título de la aplicación
st.title("Conversor de Presión")

# Input para el valor de presión
valor = st.number_input("Ingrese el valor de presión:", min_value=0.0, format="%.4f")

# Selectbox para la unidad de entrada
unidad = st.selectbox(
    "Seleccione la unidad de entrada:",
    ["atmósferas", "mm de mercurio", "milibares"]
)

# Botón para realizar la conversión
if st.button("Convertir"):
    # Convertir la presión
    atmosferas, mm_de_mercurio, milibares = convertir_presion(valor, unidad)
    
    # Crear una tabla con los resultados
    resultados = {
        "Valor calculado": [atmosferas, mm_de_mercurio, milibares],
        "Unidad": ["atmósferas", "mm de mercurio", "milibares"]
    }
    
    # Mostrar la tabla
    st.table(resultados)
