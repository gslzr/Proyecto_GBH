import requests
from Vehiculo import Vehiculo
response = requests.get("https://www.swapi.tech/api/vehicles")


class moduloVehiculo:
    def __init__(self, response):
        """
         Se crea cada vehiculo como un objeto con la informacion de la API
        """
        self.vehiculos = response.json()
        self.lista_vehiculos = []

        for i in range(len(self.vehiculos["results"])):  
            #Se obtienen los datos iniciales de el vehiculo
            vehiculos_info = {
                'uid': self.vehiculos["results"][i]["uid"],
                'name': self.vehiculos["results"][i]["name"],
                'url': self.vehiculos["results"][i]["url"]
            }
            url = vehiculos_info["url"]
            datos = requests.get(url)
            #se almacenan los datos de el vehiculo en formato json
            info = datos.json()
            
            #Se guardan los nombres de los personajes que pilotan el vehiculo en una lista
            lista_pilotos = []
            for piloto in info["result"]["properties"]["pilots"]: 
                link = requests.get(piloto)
                info_piloto = link.json()
                lista_pilotos.append(info_piloto["result"]["properties"]["name"]) 

            self.lista_vehiculos.append(Vehiculo(info["result"]["properties"]["name"], 
                                        info["result"]["properties"]["model"],
                                        lista_pilotos
                                        ))

'''
modulo = moduloVehiculo(response)
for vehiculo in modulo.lista_vehiculos:
    vehiculo.mostrar_vehiculo()
'''