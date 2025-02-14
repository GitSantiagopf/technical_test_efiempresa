import streamlit as st

# Configuración inicial de la app
st.set_page_config(page_title="Estimador de Velocidad de Pelota", page_icon="🎾", layout="wide")

# Redirigir a la página de inicio correctamente
st.switch_page("pages/home.py")  # ✅ Ahora la ruta es válida
