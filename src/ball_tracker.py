import cv2
import numpy as np
import time
from src.constants import Constants as K
from src.calculate_velocity import Calculate

class BallTracker:
    def __init__(self, source=0, output_path=None):
        self.video = cv2.VideoCapture(source)
        if not self.video.isOpened():
            raise ValueError(f"No se pudo abrir la fuente de video: {source}")

        self.fps = self.video.get(cv2.CAP_PROP_FPS) or 30.0
        self.frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.start_line = int(self.frame_height * 0.19)
        self.end_line = int(self.frame_height * 0.79)
        self.start_time = None
        self.end_time = None
        self.ball_crossed_end = False

        # Configuración mejorada del VideoWriter
        self.output_path = output_path if output_path else K.OUTPUT_PATH
        fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Codec más compatible
        self.out = cv2.VideoWriter(self.output_path, fourcc, self.fps, (self.frame_width, self.frame_height))

    def process_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return None, None

        # Procesamiento de color mejorado
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        # Operaciones morfológicas optimizadas
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # Detección de contornos con filtro de área
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        ball_position = None
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 50 and area < 5000:  # Filtro de tamaño realista
                x, y, w, h = cv2.boundingRect(cnt)
                cx, cy = x + w // 2, y + h // 2
                ball_position = (cx, cy)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        # Dibujo de líneas de referencia
        cv2.line(frame, (0, self.start_line), (self.frame_width, self.start_line), (255, 0, 0), 2)
        cv2.putText(frame, "Start (0m)", (10, self.start_line - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv2.line(frame, (0, self.end_line), (self.frame_width, self.end_line), (255, 0, 0), 2)
        cv2.putText(frame, "End (1.45m)", (10, self.end_line - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        return frame, ball_position

    def run(self):
        try:
            while self.video.isOpened():
                frame, ball_position = self.process_frame()
                if frame is None:
                    break

                # Lógica de seguimiento de tiempo
                if ball_position is not None:
                    cx, cy = ball_position
                    if self.start_time is None and cy >= self.start_line:
                        self.start_time = time.time()
                    if (self.start_time is not None 
                        and self.end_time is None 
                        and cy >= self.end_line 
                        and not self.ball_crossed_end):
                        self.end_time = time.time()
                        self.ball_crossed_end = True

                self.out.write(frame)

            # Cálculo final de velocidad
            velocidad = Calculate(self.start_time, self.end_time).calculate_velocity() if self.start_time and self.end_time else None
            
            return velocidad
            
        finally:
            # Liberación garantizada de recursos
            self.cleanup()

    def cleanup(self):
        if self.video.isOpened():
            self.video.release()
        if self.out.isOpened():
            self.out.release()
        cv2.destroyAllWindows()
        time.sleep(0.5)  # Espera crítica para liberación de archivos