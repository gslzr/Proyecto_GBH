class Especie:
    def __init__(self, nombre, altura, clasificacion,planeta_origen,lengua_materna,personajes, episodios):
        self.nombre= nombre
        self.altura= altura
        self.clasificacion= clasificacion
        self.planeta_origen= planeta_origen
        self.lengua_materna= lengua_materna
        self.personajes= personajes
        self.episodios= episodios 
        
    def mostrar_especie(self):
        print('\nNombre: ', self.nombre, '\nAltura: ', self.altura, '\nClasificacion: ', self.clasificacion, '\nPlaneta de Origen: ', self.planeta_origen, '\nLengua Materna: ', self.lengua_materna, '\nPersonajes que pertenecen a la especie: ', self.personajes, '\nEpisodios en los que aparece la especie: ', self.episodios)