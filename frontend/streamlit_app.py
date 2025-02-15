"""
streamlit_app.py

Este módulo inicia la aplicación de Streamlit y redirige automáticamente a la página principal.

Uso:
    Ejecuta el siguiente comando en la terminal para iniciar la aplicación:
    streamlit run frontend/streamlit_app.py
"""

import streamlit as st

st.set_page_config(page_title="Estimador de Velocidad de Pelota", page_icon="🎾", layout="wide")


st.switch_page("pages/home.py") 
