import requests
from Pelicula import Pelicula
response = requests.get("https://www.swapi.tech/api/films")


class moduloPelicula:
    def __init__(self, response):
        """
         Se crea cada pelicula como un objeto con la informacion de la API
        """
        self.peliculas = response.json()
        self.lista_peliculas = []

        for i in range(len(self.peliculas["result"])):  
            #Se guardan los nombres de los personajes que intervienen en la pelicula
            lista_personajes = []
            personajes = self.peliculas["result"][i]["properties"]["characters"]
            for y in range(len(personajes)): 
                link = requests.get(personajes[y])
                info_personaje = link.json()
                lista_personajes.append(info_personaje["result"]["properties"]["name"])

            #Se guardan los nombres de las especies que intervienen en la pelicula
            lista_especies = []
            for especie in self.peliculas["result"][i]["properties"]["species"]: 
                link = requests.get(especie)
                info_especie = link.json()
                #Se obtiene el nombre de la especie
                nombre_especie = info_especie["result"]["properties"]["classification"] 
                #Se verifica que la especie no se encuentre ya en la lista
                if nombre_especie not in lista_especies:
                    #Se guarda la especie en la lista de especies que aparecen en la pelicula
                    lista_especies.append(nombre_especie) 

            #Se guardan los nombres de los planetas que intervienen en la pelicula
            lista_planetas = []
            for planeta in self.peliculas["result"][i]["properties"]["planets"]: 
                link = requests.get(planeta)
                info_planeta = link.json()
                #Se obtiene el nombre del planeta
                nombre_planeta = info_planeta["result"]["properties"]["name"] 
                #Se verifica que el planeta no se encuentre ya en la lista
                if nombre_planeta not in lista_planetas:
                    #Se guarda la especie en la lista de especies que aparecen en la pelicula
                    lista_planetas.append(nombre_planeta) 

            self.lista_peliculas.append(Pelicula(self.peliculas["result"][i]["properties"]["title"], 
                                            self.peliculas["result"][i]["properties"]["episode_id"],
                                            self.peliculas["result"][i]["properties"]["release_date"],
                                            self.peliculas["result"][i]["properties"]["opening_crawl"],
                                            self.peliculas["result"][i]["properties"]["director"],
                                            lista_personajes,
                                            lista_especies, 
                                            lista_planetas
                                            ))
'''
x = moduloPelicula(response)
for i in x.lista_peliculas:
    i.mostrar_pelicula()

'''
