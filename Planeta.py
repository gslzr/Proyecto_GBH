class Planeta:
    def __init__(self,nombre, orbit_period, rotation_period, habitantes, clima, personajes, episodios):
        self.nombre = nombre
        self.orbit_period = orbit_period
        self.rotation_period = rotation_period
        self.habitantes = habitantes
        self.clima = clima
        self.personajes = personajes
        self.episodios = episodios
    
    def mostrar_planeta(self):
        print("\nNombre: ", self.nombre, "\nPeriodo de Orbita: ", self.orbit_period, "\nPeriodo de Rotacion: ", self.rotation_period, "\nHabitantes: ", self.habitantes, "\nClima: ", self.clima, "\nPersonajes originarios del planeta: ", self.personajes, "\nEpisodios en los que aparece el planeta: ", self.episodios)
