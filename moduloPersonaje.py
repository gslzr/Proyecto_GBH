import requests
from Personaje import Personaje
from moduloPelicula import moduloPelicula
from moduloNave import moduloNave
from moduloVehiculo import moduloVehiculo
from ModuloEspecie import moduloEspecie
response_especies = requests.get("https://www.swapi.tech/api/species/")
response_peliculas = requests.get("https://www.swapi.tech/api/films")
response_personajes = requests.get("https://www.swapi.tech/api/people")
response_naves = requests.get("https://www.swapi.tech/api/starships")
response_vehiculos = requests.get("https://www.swapi.tech/api/vehicles")


class moduloPersonaje:
    def __init__(self, response_personajes, moduloPelicula, moduloEspecie, moduloNave, moduloVehiculo):
        """
         Se crea cada personaje como un objeto con la informacion de la API
        """
        self.personajes = response_personajes.json()
        self.lista_personajes = []

        for i in range(len(self.personajes["results"])):  
            #Se obtienen los datos iniciales de la especie
            personajes_info = {
                'uid': self.personajes["results"][i]["uid"],
                'name': self.personajes["results"][i]["name"],
                'url': self.personajes["results"][i]["url"]
            }
            url = personajes_info["url"]
            datos = requests.get(url)
            #se almacenan los datos del personaje en formato json
            info = datos.json()
            
            #Se guardan los nombres de las naves que pilota el personaje en una lista
            naves = moduloNave
            lista_naves = []
            for nave in naves.lista_naves:
                if info["result"]["properties"]["name"] in nave.pilotos:
                    lista_naves.append(nave.nombre)  

            #Se guardan los nombres de los vehiculos que pilota el personaje en una lista
            vehiculos = moduloVehiculo
            lista_vehiculos = []
            for vehiculo in vehiculos.lista_vehiculos:
                if info["result"]["properties"]["name"] in vehiculo.pilotos:
                    lista_vehiculos.append(vehiculo.nombre)

            #Se llama a la clase moduloPelicula
            peliculas = moduloPelicula
            #Se guardan los episodios en los que ha aparecido la especie en una lista  
            lista_episodios = []
            for pelicula in peliculas.lista_peliculas:
                if info["result"]["properties"]["name"] in pelicula.personajes:
                    lista_episodios.append(pelicula.titulo)

            #Se llama a la clase moduloEspecie
            especies = moduloEspecie
            #Se guarda la especie a la que pertenece el personaje  
            especie_personaje = ""
            for especie in especies.lista_especies:
                if info["result"]["properties"]["name"] in especie.personajes:
                    especie_personaje = especie.nombre
                     
            #Se obtiene el nombre del planeta madre
            homeworld_url = info["result"]["properties"]["homeworld"]
            homeworld = requests.get(homeworld_url)
            homeworld_info = homeworld.json()
            homeworld_name = homeworld_info["result"]["properties"]["name"]

            self.lista_personajes.append(Personaje(info["result"]["properties"]["name"], 
                                            homeworld_name,
                                            info["result"]["properties"]["gender"],
                                            especie_personaje,
                                            lista_naves,
                                            lista_vehiculos,
                                            lista_episodios
                                            ))

    def buscar_personaje(self):
        #Se le pide al usuario que ingrese el nombre del personaje
        input_name = input("Ingrese el nombre del personaje que desea buscar: ").lower()
        #Se crea una lista vacia donde se guardaran todos los personajes que coincidan con la busqueda
        resultados = [] 

        for personaje in self.lista_personajes:
            #Si el input ingresado por el usuario forma parte del nombre del personaje: (se ponen tanto el input como el nombre del personaje en minuscula con .lower() para evitar que no coincidan)
            if input_name in personaje.nombre.lower():
                #Si coincide el input con parte o la totalidad del nombre del personaje, se agrega a la lista de resultados
                resultados.append(personaje)

        #Si la longitud de la lista de resultados es mayor a 0 significa que si hubo coincidencias
        if len(resultados) > 0:
            print("Personajes que coinciden con su busqueda:")
            for personaje in resultados:
                personaje.mostrar_personaje()
        else:
            print("No se encontraron personajes que coincidan con su busqueda")
'''
peliculas = moduloPelicula(response_peliculas)
vehiculos = moduloVehiculo(response_vehiculos)
naves = moduloNave(response_naves)
especies = moduloEspecie(response_especies, peliculas)
modulo = moduloPersonaje(response_personajes, peliculas, especies, naves, vehiculos)
for personaje in modulo.lista_personajes:
    personaje.mostrar_personaje()
'''

