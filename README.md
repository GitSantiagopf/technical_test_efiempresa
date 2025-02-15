#  Estimador de Velocidad de Pelota

Este proyecto permite detectar la velocidad de una pelota en un video subido por el usuario utilizando FastAPI y Streamlit.

##  Estructura del proyectp
```
project-root/
├── backend/                    # API en FastAPI para el procesamiento del video
│   ├── main.py                  # Punto de entrada de la API
│   ├── ball_tracker.py          # Detección de la pelota y cálculo de velocidad
│   ├── uploads/                 # Carpeta para almacenar videos subidos
│   ├── __init__.py              
├── frontend/                   # Interfaz en Streamlit
│   ├── streamlit_app.py         # Aplicación principal en Streamlit
│   ├── pages/                   # Subpáginas de la interfaz
│   │   ├── home.py               # Página de inicio
│   │   ├── velocity_estimation.py # Página de estimación de velocidad
│   ├── static/                  # Archivos estáticos (CSS, imágenes)
│   │   ├── style.css             # Estilos personalizados
│   ├── temp/                    # Almacenamiento temporal de videos
├── src/                         # Módulos de procesamiento
│   ├── constants.py             # Parámetros generales del sistema
│   ├── calculate_velocity.py    # Módulo para cálculo de velocidad
│   ├── __init__.py              
├── docs/                        # Documentación del proyecto
│   ├── homography.pdf           # Documento de corrección de perspectiva
│   ├── user_manual.pdf          # Manual de usuario
│   ├── technical_doc.pdf        # Documentación técnica detallada
├── tests/                       # Pruebas y experimentación
│   ├── extract_frames.py        # Extracción de frames de prueba
│   ├── ball_frames_detection.py # Pruebas de detección de pelota en frames
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Instrucciones de uso y despliegue
├── .gitignore                   # Archivos a ignorar en Git
```
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
