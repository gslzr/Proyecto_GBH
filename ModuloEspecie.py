import requests
from Especie import Especie
from moduloPelicula import moduloPelicula
response_especies = requests.get("https://www.swapi.tech/api/species/")
response_peliculas = requests.get("https://www.swapi.tech/api/films")


class moduloEspecie:
    def __init__(self, response_especies, moduloPelicula):
        """
         Se crea cada especie como un objeto con la informacion de la API
        """
        self.especies = response_especies.json()
        self.lista_especies = []

        for i in range(len(self.especies["results"])):  
            #Se obtienen los datos iniciales de la especie
            species_info = {
                'uid': self.especies["results"][i]["uid"],
                'name': self.especies["results"][i]["name"],
                'url': self.especies["results"][i]["url"]
            }
            url = species_info["url"]
            datos = requests.get(url)
            #se almacenan los datos de la especie en formato json
            info = datos.json()
            
            #Se guardan los nombres de los personajes que pertenecen a la especie en una lista
            lista_personajes = []
            lista_episodios = []
            for personaje in info["result"]["properties"]["people"]: 
                link = requests.get(personaje)
                info_personaje = link.json()
                lista_personajes.append(info_personaje["result"]["properties"]["name"])  

            #Se llama a la clase moduloPelicula
            peliculas = moduloPelicula
            #Se guardan los episodios en los que ha aparecido la especie en una lista  
            for pelicula in peliculas.lista_peliculas:
                if info["result"]["properties"]["classification"] in pelicula.especies:
                    lista_episodios.append(pelicula.titulo)

            #Se obtiene el nombre del planeta madre
            homeworld_url = info["result"]["properties"]["homeworld"]
            homeworld = requests.get(homeworld_url)
            homeworld_info = homeworld.json()
            homeworld_name = homeworld_info["result"]["properties"]["name"]

            self.lista_especies.append(Especie(info["result"]["properties"]["name"], 
                                            info["result"]["properties"]["average_height"],
                                            info["result"]["properties"]["classification"],
                                            homeworld_name,
                                            info["result"]["properties"]["language"],
                                            lista_personajes,
                                            lista_episodios
                                            ))
'''
x = moduloPelicula(response_peliculas)
modulo = moduloEspecie(response_especies, x)
for especie in modulo.lista_especies:
    especie.mostrar_especie()

'''

