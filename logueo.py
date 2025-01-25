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
            contenido_protegido()
        else:
            st.error("Nombre de usuario o contraseña incorrectos")

def signup():
    st.title("Registro de nuevo usuario")

    # Input para el nuevo nombre de usuario
    nuevo_usuario = st.text_input("Elige un nombre de usuario")

    # Input para la nueva contraseña
    nueva_contraseña = st.text_input("Elige una contraseña", type="password")

    # Input para confirmar la contraseña
    confirmar_contraseña = st.text_input("Confirma tu contraseña", type="password")

    # Botón para registrarse
    if st.button("Registrarse"):
        if nuevo_usuario in usuarios:
            st.error("El nombre de usuario ya existe. Por favor, elige otro.")
        elif nueva_contraseña != confirmar_contraseña:
            st.error("Las contraseñas no coinciden.")
        else:
            usuarios[nuevo_usuario] = nueva_contraseña
            st.success("Registro exitoso. Ahora puedes iniciar sesión.")
            st.session_state['show_login'] = True  # Mostrar el formulario de login después del registro

def contenido_protegido():
    st.title("Contenido Protegido")
    st.write(f"Bienvenido, {st.session_state['username']}!")
    st.write("Este es un contenido al que solo puedes acceder si has iniciado sesión.")

    # Botón para cerrar sesión
    if st.button("Cerrar sesión"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = None
        st.rerun()

def main():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'show_login' not in st.session_state:
        st.session_state['show_login'] = True

    # Mostrar el formulario de login o signup según el estado
    if not st.session_state['logged_in']:
        if st.session_state['show_login']:
            login()
            if st.button("¿No tienes una cuenta? Regístrate aquí"):
                st.session_state['show_login'] = False
        else:
            signup()
            if st.button("¿Ya tienes una cuenta? Inicia sesión aquí"):
                st.session_state['show_login'] = True
    else:
        contenido_protegido()

if __name__ == "__main__":
    main()
    st.text(usuarios)