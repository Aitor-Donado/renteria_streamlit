import streamlit as st

# Diccionario de usuarios y contraseñas (esto es solo un ejemplo, no es seguro para producción)
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2"
}

def login():
    st.title("Sistema de Login")

    # Input para el nombre de usuario
    usuario = st.text_input("Nombre de usuario")

    # Input para la contraseña
    contraseña = st.text_input("Contraseña", type="password")

    # Botón para iniciar sesión
    if st.button("Iniciar sesión"):
        if usuario in usuarios and usuarios[usuario] == contraseña:
            st.success("Inicio de sesión exitoso")
            st.session_state['logged_in'] = True
            st.session_state['username'] = usuario
        else:
            st.error("Nombre de usuario o contraseña incorrectos")

def contenido_protegido():
    st.title("Contenido Protegido")
    st.write(f"Bienvenido, {st.session_state['username']}!")
    st.write("Este es un contenido al que solo puedes acceder si has iniciado sesión.")

    # Botón para cerrar sesión
    if st.button("Cerrar sesión"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.experimental_rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if not st.session_state['logged_in']:
        login()
    else:
        contenido_protegido()

if __name__ == "__main__":
    main()