class Vehiculo:
    def __init__(self, nombre, modelo, pilotos):
        self.nombre = nombre  
        self.modelo = modelo  
        self.pilotos = pilotos  

    def mostrar_vehiculo(self):
        print("\nNombre: ", self.nombre,
              "\nModelo: ", self.modelo,
              "\nPilotos: ", self.pilotos)