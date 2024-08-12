class Nave:
    def __init__(self, nombre, longitud, capacidad_carga, clasificacion_hiperimpulsor, MGLT, velocidad_maxima_atmosfera, costo, pilotos):
        self.nombre = nombre
        self.longitud = longitud  
        self.capacidad_carga = capacidad_carga  
        self.clasificacion_hiperimpulsor = clasificacion_hiperimpulsor  
        self.MGLT = MGLT 
        self.velocidad_maxima_atmosfera = velocidad_maxima_atmosfera  
        self.costo = costo  
        self.pilotos = pilotos  

    def mostrar_nave(self):
        print("\nNombre: ", self.nombre,
              "\nLongitud: ", self.longitud,
              "\nCapacidad de Carga: ", self.capacidad_carga,
              "\nClasificación de Hiperimpulsor: ", self.clasificacion_hiperimpulsor,
              "\nMGLT: ", self.MGLT,
              "\nVelocidad Máxima en Atmósfera: ", self.velocidad_maxima_atmosfera,
              "\nCosto: ", self.costo,
              "\nPilotos: ", self.pilotos)
