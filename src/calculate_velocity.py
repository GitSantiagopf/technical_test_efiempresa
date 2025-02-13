from src.constants import Constants as K

class Calculate:
    def __init__(self, start_time: float, end_time: float, distance: float = K.DISTANCE_METERS):
        self.start_time = start_time
        self.end_time = end_time
        self.distance_meters = distance

    def calculate_velocity(self):
        if self.start_time is not None and self.end_time is not None:
            time_elapsed = self.end_time - self.start_time
            velocity =  self.distance_meters  / time_elapsed
            print(f"Tiempo total: {time_elapsed:.3f} segundos")
            print(f"Velocidad media estimada: {velocity:.3f} m/s")
        else:
            print("No se pudo calcular la velocidad. Verifica la detección.")
