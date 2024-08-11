import requests
from Nave import Nave
response = requests.get("https://www.swapi.tech/api/starships")


class moduloNave:
    def __init__(self, response):
        """
         Se crea cada nave como un objeto con la informacion de la API
        """
        self.naves = response.json()
        self.lista_naves = []

        for i in range(len(self.naves["results"])):  
            #Se obtienen los datos iniciales de la nave
            naves_info = {
                'uid': self.naves["results"][i]["uid"],
                'name': self.naves["results"][i]["name"],
                'url': self.naves["results"][i]["url"]
            }
            url = naves_info["url"]
            datos = requests.get(url)
            #se almacenan los datos de la nave en formato json
            info = datos.json()
            
            #Se guardan los nombres de los personajes que pilotan la nave en una lista
            lista_pilotos = []
            for piloto in info["result"]["properties"]["pilots"]: 
                link = requests.get(piloto)
                info_piloto = link.json()
                lista_pilotos.append(info_piloto["result"]["properties"]["name"]) 

            self.lista_naves.append(Nave(info["result"]["properties"]["name"], 
                                        info["result"]["properties"]["length"],
                                        info["result"]["properties"]["cargo_capacity"],
                                        info["result"]["properties"]["hyperdrive_rating"],
                                        info["result"]["properties"]["MGLT"],
                                        info["result"]["properties"]["max_atmosphering_speed"],
                                        info["result"]["properties"]["cost_in_credits"],
                                        lista_pilotos
                                        ))
'''
modulo = moduloNave(response)
for nave in modulo.lista_naves:
    nave.mostrar_nave()
'''