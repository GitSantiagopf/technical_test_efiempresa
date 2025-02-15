#  Estimador de Velocidad de Pelota

Este proyecto permite detectar la velocidad de una pelota en un video subido por el usuario utilizando FastAPI y Streamlit.

## Características

Detección de la pelota basada en color.
Cálculo automático de la velocidad en m/s.
Interfaz intuitiva con Streamlit.
Descarga del video procesado.

## Instalación y Uso

1️⃣ Clonar el repositorio e instalar librerías:
```bash
git clone https://github.com/GitSantiagopf/technical_test_efiempresa.git
cd technical_test_efiempresa/frontend
pip install -r requirements.txt
```
2️⃣ Configurar el Backend:
```bash
cd ../backend
pip install -r requirements.txt
uvicorn main:app --reload
```
3️⃣ Configurar el Frontend (En otra terminal):
```bash
cd frontend
streamlit run streamlit_app.py
```
La aplicación estará disponible en http://localhost:8501.

## API - Endpoint

🔹 Subir y procesar un video:

```bash
POST /upload/
```

Parámetro: Archivo de video (.mp4, .avi, .mov)
Respuesta:
```bash
{
  "message": "Procesamiento completo",
  "velocidad": 1.45,
  "video_path": "backend/uploads/processed_video.mp4"
}
```
Tecnologías Utilizadas

Python 3.10
FastAPI
OpenCV
Streamlit