import streamlit as st
import requests
import os


from pathlib import Path

st.set_page_config(page_title="Estimador de Velocidad", page_icon="⚡", layout="wide")

# Obtener la ruta absoluta del archivo CSS
css_path = Path(__file__).parent.parent / "static/style.css"

if css_path.exists():
    with open(css_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.error(f"❌ No se encontró el archivo de estilos CSS en {css_path}")

st.markdown("<h1 class='title'>🎾 Estimación de Velocidad</h1>", unsafe_allow_html=True)


API_URL = "http://127.0.0.1:8000/upload/"

video_file = st.file_uploader("📂 Selecciona un archivo", type=["mp4", "avi", "mov"])

if video_file is not None:
    save_path = os.path.join("..", "frontend", "temp", video_file.name)
    os.makedirs(os.path.join("..", "frontend", "temp"), exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(video_file.read())
    st.success("✅ Video cargado correctamente.")

    if st.button("⚡ Procesar Video", use_container_width=True):
        with st.spinner("Procesando..."):
            with open(save_path, "rb") as file:
                response = requests.post(API_URL, files={"video": file})
            
            if response.status_code == 200:
                data = response.json()
                velocidad = data["velocidad"]
                video_path = data["video_path"]
                st.markdown(f"<h2 class='result'>⚡ Velocidad: {velocidad:.3f} m/s</h2>", unsafe_allow_html=True)
                
                # Botón para descargar el video procesado
                if os.path.exists(video_path) and os.path.getsize(video_path) > 0:
                    with open(video_path, "rb") as processed_file:
                        st.download_button(
                            label="⬇️ Descargar Video Procesado",
                            data=processed_file,
                            file_name="output.mp4",
                            mime="video/mp4",
                            use_container_width=True
                        )
                else:
                    st.error("❌ El video no se generó correctamente.")
            else:
                st.error("❌ Error al procesar el video.")

if st.button("🏠 Volver al Inicio", use_container_width=True):
    st.switch_page("pages/home.py")
