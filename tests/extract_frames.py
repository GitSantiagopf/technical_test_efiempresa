import cv2
import os

video_path = "./video.mp4"
output_folder = "./frames_extracted"
os.makedirs(output_folder, exist_ok=True)
video = cv2.VideoCapture(video_path)
frame_indices = [10, 30, 50, 70, 90]
frame_id = 0

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    if frame_id in frame_indices:
        frame_filename = os.path.join(output_folder, f"frame_{frame_id}.jpg")
        cv2.imwrite(frame_filename, frame) 
        print(f"Frame {frame_id} guardado en {frame_filename}")
    frame_id += 1
    if frame_id > max(frame_indices):
        break
video.release()
cv2.destroyAllWindows()
print(f"Frames extraídos en: {output_folder}")
