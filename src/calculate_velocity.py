"""
calculate_velocity.py

Este módulo contiene la clase `Calculate`, que se encarga de calcular la velocidad de una pelota basándose en los tiempos de inicio y fin de su recorrido.

Uso:
    from src.calculate_velocity import Calculate
    velocidad = Calculate(start_time=1.0, end_time=2.5).calculate_velocity()
    print(velocidad)
"""

from src.constants import Constants as K

class Calculate:
    """
    Clase para calcular la velocidad de la pelota con base en los tiempos de recorrido.

    Attributes:
        start_time (float): Tiempo en segundos cuando la pelota cruza la primera línea.
        end_time (float): Tiempo en segundos cuando la pelota cruza la segunda línea.
        distance_meters (float): Distancia en metros entre las dos líneas de referencia.

    Methods:
        calculate_velocity():
            Calcula y retorna la velocidad de la pelota en metros por segundo (m/s).
    """
    def __init__(self, start_time: float, 
                end_time: float,
                distance: float = K.DISTANCE_METERS):
        """
        Inicializa la clase.
        Args:
            start_time (float): Momento en que la pelota cruza la primera línea.
            end_time (float): Momento en que la pelota cruza la segunda línea.
            distance (float, opcional): Distancia entre las dos líneas en metros. Por defecto, se usa `Constants.DISTANCE_METERS`.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.distance_meters = distance

    def calculate_velocity(self):
        """
        Calcula la velocidad de la pelota en metros por segundo (m/s).

        Returns:
            float: Velocidad calculada en m/s si los tiempos son válidos, de lo contrario, None.
        """
        if self.start_time is not None and self.end_time is not None:
            time_elapsed = self.end_time - self.start_time
            velocity = K.DISTANCE_METERS / time_elapsed
            print(f"Tiempo total: {time_elapsed:.3f} segundos")
            print(f"Velocidad media estimada: {velocity:.3f} m/s")
            return velocity
        else:
            print("No se pudo calcular la velocidad. Verifica la detección.")
            return None
