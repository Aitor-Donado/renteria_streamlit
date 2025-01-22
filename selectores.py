import streamlit as st

# Inicializar el diccionario 'usuario' en session_state si no existe
if 'usuario' not in st.session_state:
    st.session_state.usuario = {}

def ha_cambiado():
    """
    Función que se ejecuta al cambiar el estado del checkbox
    """
    print("Ha cambiado el checkbox")
    # Imprime el estado del checkbox llamado chequeador
    st.session_state.usuario["VMailPlan"] = st.session_state.vmail
    st.session_state.usuario["IntlPlan"] = st.session_state.intl
    print(st.session_state.usuario)

def intro_pais():
    print(st.session_state.pais)
    st.session_state.usuario["País"] = st.session_state.pais
    print(st.session_state.usuario)

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
radio_btn = st.radio("Marca tu país", 
                     options = opciones, 
                     on_change=intro_pais,
                     key="pais")

# Imprimirá el valor de la tupla seleccionado al cambiarlo
# print(radio_btn)
# También se le puede asociar un "on_change" y "key" como al anterior

st.divider()

# Es un selector desplegable que sólo permite una elección
opciones = ("Renault 5", "Seat 127", "Fiat 500")
select = st.selectbox("Elige tu coche favorito", options= opciones)
print(select)

# Es un selector desplegable que permite varias opciones
opciones = ("Renault 5", "Seat 127", "Fiat 500")
multi_select = st.multiselect("Elige tus coches favoritos", options= opciones)
st.write(multi_select)


valor = st.slider("Deslizante", min_value=50, max_value=150, value=75)
print(valor)

opciones = ['infrared', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
start_color, end_color = st.select_slider('Selecciona un color',
                                            options=opciones,
                                            value=('red', 'blue'))
st.write(f'Has seleccionado entre {start_color} y {end_color}')
