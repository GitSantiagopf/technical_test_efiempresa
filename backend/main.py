"""
main.py

Este módulo inicia el servidor FastAPI para procesar videos y calcular la velocidad 
de una pelota en movimiento utilizando el detector `BallTracker`.`BallTracker`

Endpoints:
    - `POST /upload/`: Recibe un video, lo procesa y devuelve la velocidad estimada.

"""
from fastapi import FastAPI, UploadFile, File
import os
import shutil
import uvicorn
from backend.ball_tracker import BallTracker

app = FastAPI()

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_video(video: UploadFile = File(...), distance_real: float = 1.45):
    """
    Recibe un video subido por el usuario, lo guarda en el servidor, procesa la detección 
    de la pelota y calcula su velocidad.
    Args:
        video (UploadFile): Archivo de video en formato `.mp4`, `.avi` o `.mov`.
    Returns:
        dict: Contiene un mensaje de confirmación, la velocidad estimada y la ruta del video procesado.
    """
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    
    output_video_path = os.path.join(UPLOAD_FOLDER, "processed_" + video.filename)
    tracker = BallTracker(source=video_path, output_path=output_video_path, distance_real = distance_real)
    velocidad = tracker.run()
    
    print(f"Recibiendo video: {video.filename}")
    print(f"Video guardado en: {video_path}")
    print(f"Velocidad calculada: {velocidad}")
    
    if velocidad is None:
        velocidad = 0

    return {"message": "Procesamiento completo", "velocidad": velocidad, "video_path": output_video_path}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
