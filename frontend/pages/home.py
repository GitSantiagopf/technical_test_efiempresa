"""
home.py

Este módulo proporciona la pantalla de inicio de la aplicación Streamlit, donde los usuarios pueden acceder a la funcionalidad de estimación de velocidad de la pelota.

"""
import streamlit as st
import os
import time

st.set_page_config(page_title="Inicio - Estimador de Velocidad", page_icon="🏠", layout="wide")
css_path = os.path.join(os.path.dirname(__file__), "../static/style.css")

if os.path.exists(css_path): 
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error("No se encontró el archivo de estilos CSS.")

st.markdown("""
    <h1 class="title">Bienvenido al Estimador de Velocidad de Pelota</h1>
    <p class="subtitle">Sube un video y descubre la velocidad de la pelota en tiempo real.</p>
""", unsafe_allow_html=True)

distance_real = st.number_input("📏 Distancia real entre líneas de referencia (metros):", min_value=0.1, value=1.45, step=0.01)

st.markdown("<div class='center'>", unsafe_allow_html=True)
if st.button("Estimar Velocidad de Pelota", use_container_width=True):
    st.session_state["distance_real"] = distance_real
    st.switch_page("pages/velocity_estimation.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    ### 📌 ¿Tu cámara no está completamente alineada con la trayectoria?
    Si la perspectiva de la cámara no es totalmente paralela u ortogonal al plano, es recomendable aplicar **corrección de homografía** y definir las líneas de referencia para una mejor estimación de velocidad.
""")
st.markdown("[📖 Leer más sobre corrección de perspectiva](https://github.com/GitSantiagopf/technical_test_efiempresa/blob/main/docs/Homografy.pdf)")

st.markdown("<p class='footer'>Estimador de Velocidad</p>", unsafe_allow_html=True)
