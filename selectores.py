import streamlit as st

usuario = {}

def ha_cambiado():
    """
    Función que se ejecuta al cambiar el estado del checkbox
    """
    print("Ha cambiado el checkbox")
    # Imprime el estado del checkbox llamado chequeador
    usuario["VMailPlan"] = st.session_state.vmail
    usuario["IntlPlan"] = st.session_state.intl
    print(usuario)

state = st.checkbox("El usuario tiene plan de Mail",
    value=True,
    on_change = ha_cambiado,
    key = "vmail")

state = st.checkbox("El usuario tiene llamadas internacionales",
    value=True,
    on_change = ha_cambiado,
    key = "intl")

# Sólo permite seleccionar uno
opciones = ("España", "Cuba", "Venezuela")
radio_btn = st.radio("Marca tu país", options = opciones)
# Imprimirá el valor de la tupla seleccionado al cambiarlo
print(radio_btn)
# También se le puede asociar un "on_change" y "key" como al anterior