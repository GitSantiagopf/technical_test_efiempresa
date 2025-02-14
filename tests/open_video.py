import cv2

video_path = "output_videos/output.mp4"
video = cv2.VideoCapture(video_path)

if video.isOpened():
    print("✅ OpenCV puede abrir el archivo sin problemas.")
else:
    print("❌ OpenCV NO puede acceder al archivo. Posible bloqueo del SO.")
