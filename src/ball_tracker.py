import cv2
import numpy as np
import time
from src.constants import Constants as K
from src.calculate_velocity import Calculate

class BallTracker:
    def __init__(self):
        self.video = cv2.VideoCapture(K.VIDEO_PATH)
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.frame_width = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.start_line = int(self.frame_height * 0.19)  
        self.end_line = int(self.frame_height * 0.79) 
        self.start_time = None
        self.end_time = None
        self.ball_crossed_end = False 
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter(K.OUTPUT_PATH, fourcc, self.fps, (self.frame_width, self.frame_height))
        self.setup_window()
    def setup_window(self):
        cv2.namedWindow("Ball Detection", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Ball Detection", 600, 1024)
        
    def process_frame(self):
        ret, frame = self.video.read()
        if not ret:
            return None, None  # Evita error de desempaquetado

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([90, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        ball_position = None
        for cnt in contours:
            if cv2.contourArea(cnt) > 50:
                x, y, w, h = cv2.boundingRect(cnt)
                cx, cy = x + w // 2, y + h // 2
                ball_position = (cx, cy)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

        cv2.line(frame, (0, self.start_line), (self.frame_width, self.start_line), (255, 0, 0), 2)
        cv2.putText(frame, "Start (0m)", (10, self.start_line - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        cv2.line(frame, (0, self.end_line), (self.frame_width, self.end_line), (255, 0, 0), 2)
        cv2.putText(frame, "End (1.45m)", (10, self.end_line - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

        return frame, ball_position

    def run(self):
        while self.video.isOpened():
            result = self.process_frame()
            if result is None:
                break 
            frame, ball_position = result

            if ball_position is not None:
                cx, cy = ball_position 
                
                if self.start_time is None and cy >= self.start_line:
                    self.start_time = time.time()
                    print(f"Inicio del recorrido: {self.start_time:.3f} segundos")

                if (self.start_time is not None and self.end_time is None and 
                    cy >= self.end_line and not self.ball_crossed_end):
                    self.end_time = time.time()
                    self.ball_crossed_end = True
                    print(f"Final del recorrido (Primer cruce): {self.end_time:.3f} segundos")

            if frame is not None:
                self.out.write(frame)
                cv2.imshow("Ball Detection", frame)

            if (cv2.waitKey(1) & 0xFF == ord("q"))|(frame is None):
                break

        Calculate(start_time= self.start_time, end_time=self.end_time).calculate_velocity() 
        self.cleanup()

    def cleanup(self):
        self.video.release()
        self.out.release()
        cv2.destroyAllWindows()
        print(f"Procesamiento completado. Video guardado en {K.OUTPUT_PATH}")

