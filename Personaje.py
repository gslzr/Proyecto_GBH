class Personaje:
    def __init__(self,nombre, planeta_origen, genero, especie, naves, vehiculos, episodios):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.genero = genero
        self.especie = especie
        self.naves = naves
        self.vehiculos = vehiculos
        self.episodios = episodios

    def mostrar_personaje(self):
        print("\nNombre: ", self.nombre, "\nPlaneta Origen: ", self.planeta_origen, "\nGenero: ", self.genero, "\nEspecie: ", self.especie, "\nNaves que utiliza: ", self.naves, "\nVehiculos que utiliza: ", self.vehiculos, "\nEpisodios en los que aparece el personaje: ", self.episodios)
