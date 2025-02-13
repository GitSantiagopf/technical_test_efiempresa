import cv2
import numpy as np
import matplotlib.pyplot as plt

frame_paths = {
    "Frame 10": "./frames_extracted/frame_10.jpg",
    "Frame 30": "./frames_extracted/frame_30.jpg",
    "Frame 50": "./frames_extracted/frame_50.jpg",
    "Frame 70": "./frames_extracted/frame_70.jpg",
    "Frame 90": "./frames_extracted/frame_90.jpg"
}
processed_frames = {}

for label, path in frame_paths.items():
    frame = cv2.imread(path)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 50:  
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    processed_frames[label] = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

fig, axes = plt.subplots(1, len(processed_frames), figsize=(20, 10))
for i, (label, img) in enumerate(processed_frames.items()):
    axes[i].imshow(img)
    axes[i].axis("off")
    axes[i].set_title(label)
plt.show()
