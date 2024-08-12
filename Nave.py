class Nave:
    def __init__(self, longitud, capacidad_carga, clasificacion_hiperimpulsor, mglT, velocidad_maxima_atmosfera, costo, pilotos):
        self.longitud = longitud  # Longitud de la nave
        self.capacidad_carga = capacidad_carga  # Capacidad de carga
        self.clasificacion_hiperimpulsor = clasificacion_hiperimpulsor  # Clasificación de hiperimpulsor
        self.mglT = mglT  # Modern Galactic Light Time
        self.velocidad_maxima_atmosfera = velocidad_maxima_atmosfera  # Velocidad máxima en atmósfera
        self.costo = costo  # Costo
        self.pilotos = pilotos  # Pilotos

    def mostrar_nave(self):
        print("\nLongitud: ", self.longitud,
              "\nCapacidad de Carga: ", self.capacidad_carga,
              "\nClasificación de Hiperimpulsor: ", self.clasificacion_hiperimpulsor,
              "\nMGLT: ", self.mglT,
              "\nVelocidad Máxima en Atmósfera: ", self.velocidad_maxima_atmosfera,
              "\nCosto: ", self.costo,
              "\nPilotos: ", self.pilotos)
