from fastapi import FastAPI, UploadFile, File
import os
import shutil
import uvicorn
from backend.ball_tracker import BallTracker

app = FastAPI()

# Carpeta para guardar los videos subidos y procesados
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_video(video: UploadFile = File(...)):
    """Recibe un video, lo guarda y procesa la velocidad de la pelota."""
    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    
    # Procesar el video con BallTracker
    output_video_path = os.path.join(UPLOAD_FOLDER, "processed_" + video.filename)
    tracker = BallTracker(source=video_path, output_path=output_video_path)
    velocidad = tracker.run()
    
    print(f"📥 Recibiendo video: {video.filename}")
    print(f"✅ Video guardado en: {video_path}")
    print(f"⚡ Velocidad calculada: {velocidad}")
    
    # Si no se detectó la velocidad, devolvemos 0
    if velocidad is None:
        velocidad = 0

    return {"message": "Procesamiento completo", "velocidad": velocidad, "video_path": output_video_path}

if __name__ == "__main__":
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
