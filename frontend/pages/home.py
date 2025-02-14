import streamlit as st
import os
import time

st.set_page_config(page_title="Inicio - Estimador de Velocidad", page_icon="🏠", layout="wide")

# Cargar estilos CSS con una ruta absoluta
css_path = os.path.join(os.path.dirname(__file__), "../static/style.css")

if os.path.exists(css_path):  # Verifica si el archivo existe
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error("No se encontró el archivo de estilos CSS.")

st.markdown("""
    <h1 class="title">Bienvenido al Estimador de Velocidad de Pelota</h1>
    <p class="subtitle">Sube un video y descubre la velocidad de la pelota en tiempo real.</p>
""", unsafe_allow_html=True)

st.markdown("<div class='center'>", unsafe_allow_html=True)
if st.button("Estimar Velocidad de Pelota", use_container_width=True):
    st.switch_page("pages/velocity_estimation.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<p class='footer'>Estimador de Velocidad</p>", unsafe_allow_html=True)
