import requests
from Planeta import Planeta
from moduloPelicula import moduloPelicula
from moduloPersonaje import moduloPersonaje
from moduloVehiculo import moduloVehiculo
from ModuloEspecie import moduloEspecie
from moduloNave import moduloNave
response_especies = requests.get("https://www.swapi.tech/api/species/")
response_peliculas = requests.get("https://www.swapi.tech/api/films")
response_planetas = requests.get("https://www.swapi.tech/api/planets")
response_personajes = requests.get("https://www.swapi.tech/api/people")
response_naves = requests.get("https://www.swapi.tech/api/starships")
response_vehiculos = requests.get("https://www.swapi.tech/api/vehicles")

class moduloPlaneta:
    def __init__(self, response_planetas, moduloPelicula, moduloPersonaje):
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
            
            #Se crean lista para guardar los personajes originarios del planeta y los episodios donde ha aparecido el planeta respectivamente
            lista_personajes = []
            lista_episodios = []

            #Se llama a la clase moduloPelicula
            peliculas = moduloPelicula
            #Se itera sobre cada objeto de tipo pelicula 
            for pelicula in peliculas.lista_peliculas:
                #Si el nombre del planeta se encuentra en la lista de planetas que aparecen en el episodio:
                if info["result"]["properties"]["name"] in pelicula.planetas:
                    #Se guardan los episodios en los que ha aparecido el planeta en una lista 
                    lista_episodios.append(pelicula.titulo)

            #Se llama a la clase moduloPersonaje
            personajes = moduloPersonaje
            #Se itera sobre cada objeto de tipo personaje 
            for personaje in personajes.lista_personajes:
                #Si el nombre del planeta coincide con el planeta origen del personaje, se guarda el nombre del personaje en una lista
                if info["result"]["properties"]["name"] == personaje.planeta_origen: 
                    lista_personajes.append(personaje.nombre)

            
            self.lista_planetas.append(Planeta(info["result"]["properties"]["name"], 
                                                        info["result"]["properties"]["orbital_period"],
                                                        info["result"]["properties"]["rotation_period"],
                                                        info["result"]["properties"]["population"],
                                                        info["result"]["properties"]["climate"],
                                                        lista_personajes,
                                                        lista_episodios
                                                        ))

'''
peliculas = moduloPelicula(response_peliculas)
vehiculos = moduloVehiculo(response_vehiculos)
naves = moduloNave(response_naves)
especies = moduloEspecie(response_especies, peliculas)
personajes = moduloPersonaje(response_personajes, peliculas, especies, naves, vehiculos)
modulo_planetas = moduloPlaneta(response_planetas, peliculas, personajes)
for planeta in modulo_planetas.lista_planetas:
    planeta.mostrar_planeta()
'''

