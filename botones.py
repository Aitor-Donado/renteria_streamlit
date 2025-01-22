import streamlit as st
# Desencadenar acciones al pulsar el botón

boton = st.button("Pulsa", on_click = lambda: print("Pulsado"))

# Descargar un objeto
text_contents = '''Texto que se descargará'''
st.download_button('Descarga archivo de texto', text_contents)

# Enlace a página
st.link_button("Galería de plantillas para streamlit",
"https://streamlit.io/gallery")

import time
# La barra empieza en 0 y le doy valores de 1 en 1 cada decima de segundo
progress_text = "La operacion se está realizando. Espere."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1, text=progress_text)

time.sleep(1)
my_bar.empty()
st.button("Rerun")