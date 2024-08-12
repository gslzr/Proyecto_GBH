import requests
from Planeta import Planeta
from moduloPelicula import moduloPelicula
from moduloPersonaje import moduloPersonaje
from moduloVehiculo import moduloVehiculo
from ModuloEspecie import moduloEspecie
from moduloNave import moduloNave
from moduloPlaneta import moduloPlaneta
response_especies = requests.get("https://www.swapi.tech/api/species/")
response_peliculas = requests.get("https://www.swapi.tech/api/films")
response_planetas = requests.get("https://www.swapi.tech/api/planets")
response_personajes = requests.get("https://www.swapi.tech/api/people")
response_naves = requests.get("https://www.swapi.tech/api/starships")
response_vehiculos = requests.get("https://www.swapi.tech/api/vehicles")

peliculas = moduloPelicula(response_peliculas)
vehiculos = moduloVehiculo(response_vehiculos)
naves = moduloNave(response_naves)
especies = moduloEspecie(response_especies, peliculas)
personajes = moduloPersonaje(response_personajes, peliculas, especies, naves, vehiculos)
planetas = moduloPlaneta(response_planetas, peliculas, personajes)

while True:
    opcion_menu = input("\nBienvenido al módulo de información de la saga Star Wars. ¿Qué acción desea realizar? \n1. Ver lista de películas de la saga \n2. Ver lista de especies de seres vivos de la saga \n3. Ver lista de planetas \n4. Buscar personaje \n5. Salir")

    if opcion_menu == "1":
        for pelicula in peliculas.lista_peliculas:
            pelicula.mostrar_pelicula()

    elif opcion_menu == "2":
        for especie in especies.lista_especies:
            especie.mostrar_especie()

    elif opcion_menu == "3":
        for planeta in planetas.lista_planetas:
            planeta.mostrar_planeta()

    elif opcion_menu == "4":
        personajes.buscar_personaje()

    elif opcion_menu == "6":
        print("¡Hasta luego!")
        break

    else: 
        print("\nIngrese una opción válida.")

