import streamlit as st

st.image("imagenes/arbol.png", caption = "Árbol de decisión", width = 650)
st.audio("imagenes/musica.mp3")
st.video("imagenes/sample.mp4")


# Modificaciones de estilo
# Vamos a centrar un título en una página
# Podemos hacerlo con cualquier otra clase de elemento
st.markdown("# Título de una página")
st.markdown("""
<style>
  h1[level="1"] {text-align: center;}
</style>
""", unsafe_allow_html = True)

st.markdown("# Otro Título")
st.markdown("""
<style>
  h1[id="89635377"] {
    background-color: #FFFFFF !important;
    color: #FF0000 !important;
  }
</style>
""", unsafe_allow_html=True)