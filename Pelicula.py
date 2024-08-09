class Pelicula:
    def __init__(self,titulo, num_episodio, fecha_lanzamiento, opening_crawl, director, personajes, especies):
        self.titulo = titulo
        self.num_episodio = num_episodio
        self.fecha_lanzamiento = fecha_lanzamiento
        self.opening_crawl = opening_crawl
        self.director = director
        self.personajes = personajes
        self.especies = especies
    
    def mostrar_pelicula(self):
        print("\nTitulo: ", self.titulo, "\nNúmero de episodio: ", self.num_episodio, "\nFecha de lanzamiento: ", self.fecha_lanzamiento, "\nOpening Crawl: ", self.opening_crawl, "\nDirector: ", self.director, "\nPersonajes: ", self.personajes, "\nEspecies: ", self.especies)
