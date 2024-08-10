import requests
from Especie import Especie
from moduloPelicula import moduloPelicula
response_especies = requests.get("https://www.swapi.tech/api/species/")
response_peliculas = requests.get("https://www.swapi.tech/api/films")
response_planetas = requests.get("https://www.swapi.tech/api/planets")

class moduloPlaneta:
    def __init__(self, response_planetas, moduloPelicula):
        """
         Se crea cada planeta como un objeto con la informacion de la API
        """
        #Se guarda la informacion de la API en formato json
        self.planetas = response_planetas.json()
        #Se crea una lista vacia donde se almacenaran todos los objetos de tipo planeta
        self.lista_planetas = []

        for i in range(len(self.planetas["results"])):  
            #Se obtienen los datos iniciales del planeta
            planets_info = {
                'uid': self.planetas["results"][i]["uid"],
                'name': self.planetas["results"][i]["name"],
                'url': self.planetas["results"][i]["url"]
            }
            url = planets_info["url"]
            datos = requests.get(url)
            #se almacenan los datos del planeta en formato json
            info = datos.json()
            
            #Se guardan los nombres de los personajes originarios del planeta en una lista
            lista_personajes = []
            lista_episodios = []

            #Se llama a la clase moduloPelicula
            peliculas = moduloPelicula
            #Se itera sobre cada objeto de tipo pelicula 
            for pelicula in peliculas.lista_peliculas:
                if info["result"]["properties"]["name"] in pelicula.planetas:
                    #Se guardan los episodios en los que ha aparecido la especie en una lista 
                    lista_episodios.append(pelicula.titulo)

'''
            self.lista_especies.append(Especie(info["result"]["properties"]["name"], 
                                                        info["result"]["properties"]["average_height"],
                                                        info["result"]["properties"]["classification"],
                                                        homeworld_name,
                                                        info["result"]["properties"]["language"],
                                                        lista_personajes,
                                                        lista_episodios
                                                        ))
'''

            
'''
x = moduloPelicula(response_peliculas)
modulo = moduloEspecie(response_especies, x)
for especie in modulo.lista_especies:
    especie.mostrar_especie()

'''