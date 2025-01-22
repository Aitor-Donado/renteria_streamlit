import streamlit as st

st.markdown("<h1 style='text-align: center;'>Registro de Usuario</h1>", unsafe_allow_html=True)

# Crear el formulario
with st.form("Formulario", clear_on_submit=True):
    col1, col2 = st.columns(2)

    # Entradas del formulario
    primer_nombre = col1.text_input("Nombre")
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
    if not all([primer_nombre, 
                apellido, 
                correo, 
                contraseña, 
                confirmar_contraseña]):
        st.warning("Por favor, complete todos los campos.")
    elif contraseña != confirmar_contraseña:
        st.error("Las contraseñas no coinciden.")
    else:
        datos_usuario = {
            "Primer Nombre": primer_nombre,
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