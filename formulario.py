import streamlit as st
import re

# Expresión regular para validar el correo electrónico
patron_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# Título centrado
st.markdown("<h1 style='text-align: center;'>Registro de Usuario</h1>", unsafe_allow_html=True)

# Crear el formulario
with st.form("Formulario", clear_on_submit=True):  # Limpiar el formulario al enviar
    col1, col2 = st.columns(2)

    # Entradas del formulario
    nombre = col1.text_input("Nombre")
    apellido = col2.text_input("Apellidos")
    correo = st.text_input("Correo Electrónico")
    contraseña = st.text_input("Contraseña", type="password")
    confirmar_contraseña = st.text_input("Confirmar Contraseña", type="password")

    dia, mes, año = st.columns(3)
    dia_nacimiento = dia.text_input("Día")
    mes_nacimiento = mes.text_input("Mes")
    año_nacimiento = año.text_input("Año")

    # Botón de envío
    enviado = st.form_submit_button("Enviar")

# Mostrar los datos en formato JSON si se envía el formulario
if enviado:
    if not all([nombre, apellido, correo, contraseña, confirmar_contraseña]):
        st.warning("Por favor, complete todos los campos.")
    elif contraseña != confirmar_contraseña:
        st.error("Las contraseñas no coinciden.")
    elif not re.fullmatch(patron_email, correo):
        st.error("El email no es correcto.")
    else:
        datos_usuario = {
            "Primer Nombre": nombre,
            "Apellido": apellido,
            "Correo Electrónico": correo,
            "Fecha de Nacimiento": {
                "Día": dia_nacimiento,
                "Mes": mes_nacimiento,
                "Año": año_nacimiento
            }
        }
        st.success("Formulario enviado con éxito!")
        st.json(datos_usuario)