import requests
<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import csv
from statistics import mean, mode
=======
>>>>>>> main
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
<<<<<<< HEAD
            


    def grafico_longitud(self):
        #Se crea la lista donde se almacenan los datos a representar de cada nave
        data = []
        for nave in self.lista_naves:
            datos_planeta = {"NOMBRE NAVE": nave.nombre, "LONGITUD": nave.longitud}
            data.append(datos_planeta)

        #Se crea el archivo .csv llamado longitud_naves.csv, y se utiliza el parametro "w" para indicar que vamos a escribir datos sobre el archivo
        with open('longitud_naves.csv', 'w', newline='') as csvfile:
            #Se definen los titulos de las columnas
            campos = ["NOMBRE NAVE", "LONGITUD"]
            #Se utiliza la clase DictWriter para escribir los campos definidos como los nombres de las columnas, y la data de los diccionarios como las filas del csv
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            #Se escribe la cabecera del archivo
            writer.writeheader()
            #Se llenan las filas con la informacion de las naves
            writer.writerows(data)

        datos = pd.read_csv('longitud_naves.csv') 
  
        df = pd.DataFrame(datos) 
        
        #Se asignan que datos se representaran en el eje X y en el eje Y
        X = list(df.iloc[:, 0]) 
        Y = list(df.iloc[:, 1]) 
        
        #Se crea el gráfico de barras
        fig, ax = plt.subplots()
        ax.bar(X, Y, color='c') 

        #Se desactiva la notación científica en el eje y
        ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

        ax.set_title("COMPARACIÓN LONGITUD NAVES") 
        ax.set_xlabel("NOMBRE NAVE") 
        ax.set_ylabel("LONGITUD") 


        #Se ajusta el tamaño de la fuente:
        font = {'size': 6}
        plt.rc('font', **font)
        
        #Se visualiza el gráfico
        plt.show()

    def grafico_capacidad_carga(self):
        #Se crea la lista donde se almacenan los datos a representar de cada nave
        data = []
        for nave in self.lista_naves:
            datos_planeta = {"NOMBRE NAVE": nave.nombre, "CAPACIDAD DE CARGA": nave.capacidad_carga}
            data.append(datos_planeta)

        #Se crea el archivo .csv llamado longitud_naves.csv, y se utiliza el parametro "w" para indicar que vamos a escribir datos sobre el archivo
        with open('capacidad_carga_naves.csv', 'w', newline='') as csvfile:
            #Se definen los titulos de las columnas
            campos = ["NOMBRE NAVE", "CAPACIDAD DE CARGA"]
            #Se utiliza la clase DictWriter para escribir los campos definidos como los nombres de las columnas, y la data de los diccionarios como las filas del csv
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            #Se escribe la cabecera del archivo
            writer.writeheader()
            #Se llenan las filas con la informacion de las naves
            writer.writerows(data)

        datos = pd.read_csv('capacidad_carga_naves.csv') 
  
        df = pd.DataFrame(datos) 
        
        #Se asignan que datos se representaran en el eje X y en el eje Y
        X = list(df.iloc[:, 0]) 
        Y = list(df.iloc[:, 1]) 
        
        #Se crea el grafico de barras 
        plt.bar(X, Y, color='c') 
        plt.title("COMPARACIÓN CAPACIDAD DE CARGA NAVES") 
        plt.xlabel("NOMBRE NAVE") 
        plt.ylabel("CAPACIDAD DE CARGA") 

        #Se ajusta el tamaño de la fuente:
        font = {'size': 6}
        plt.rc('font', **font)
        
        plt.ticklabel_format(style='plain', axis='y')  # Esto desactiva la notación científica

        #Se visualiza el gráfico
        plt.show()

    def grafico_hiperimpulsor(self):
        #Se crea la lista donde se almacenan los datos a representar de cada nave
        data = []
        for nave in self.lista_naves:
            datos_planeta = {"NOMBRE NAVE": nave.nombre, "CAPACIDAD DE HIPERIMPULSOR": nave.clasificacion_hiperimpulsor}
            data.append(datos_planeta)

        #Se crea el archivo .csv llamado longitud_naves.csv, y se utiliza el parametro "w" para indicar que vamos a escribir datos sobre el archivo
        with open('hiperimpulsor_naves.csv', 'w', newline='') as csvfile:
            #Se definen los titulos de las columnas
            campos = ["NOMBRE NAVE", "CAPACIDAD DE HIPERIMPULSOR"]
            #Se utiliza la clase DictWriter para escribir los campos definidos como los nombres de las columnas, y la data de los diccionarios como las filas del csv
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            #Se escribe la cabecera del archivo
            writer.writeheader()
            #Se llenan las filas con la informacion de las naves
            writer.writerows(data)

        datos = pd.read_csv('hiperimpulsor_naves.csv') 
  
        df = pd.DataFrame(datos) 
        
        #Se asignan que datos se representaran en el eje X y en el eje Y
        X = list(df.iloc[:, 0]) 
        Y = list(df.iloc[:, 1]) 
        
        #Se crea el grafico de barras 
        plt.bar(X, Y, color='c') 
        plt.title("COMPARACIÓN HIPERIMPULSOR NAVES") 
        plt.xlabel("NOMBRE NAVE") 
        plt.ylabel("CAPACIDAD DE HIPERIMPULSOR") 

        #Se ajusta el tamaño de la fuente:
        font = {'size': 6}
        plt.rc('font', **font)
        
        plt.ticklabel_format(style='plain', axis='y')  # Esto desactiva la notación científica

        #Se visualiza el gráfico
        plt.show()

    def grafico_MGLT(self):
        #Se crea la lista donde se almacenan los datos a representar de cada nave
        data = []
        for nave in self.lista_naves:
            datos_planeta = {"NOMBRE NAVE": nave.nombre, "MGLT": nave.MGLT}
            data.append(datos_planeta)

        #Se crea el archivo .csv llamado longitud_naves.csv, y se utiliza el parametro "w" para indicar que vamos a escribir datos sobre el archivo
        with open('MGLT_naves.csv', 'w', newline='') as csvfile:
            #Se definen los titulos de las columnas
            campos = ["NOMBRE NAVE", "MGLT"]
            #Se utiliza la clase DictWriter para escribir los campos definidos como los nombres de las columnas, y la data de los diccionarios como las filas del csv
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            #Se escribe la cabecera del archivo
            writer.writeheader()
            #Se llenan las filas con la informacion de las naves
            writer.writerows(data)

        datos = pd.read_csv('MGLT_naves.csv') 
  
        df = pd.DataFrame(datos) 
        
        #Se asignan que datos se representaran en el eje X y en el eje Y
        X = list(df.iloc[:, 0]) 
        Y = list(df.iloc[:, 1]) 
        
        #Se crea el grafico de barras 
        plt.bar(X, Y, color='c') 
        plt.title("COMPARACIÓN MGLT NAVES") 
        plt.xlabel("NOMBRE NAVE") 
        plt.ylabel("MGLT") 

        #Se ajusta el tamaño de la fuente:
        font = {'size': 6}
        plt.rc('font', **font)
        
        plt.ticklabel_format(style='plain', axis='y')  # Esto desactiva la notación científica

        #Se visualiza el gráfico
        plt.show()

    def tabla_estadisticas(self):
        nombres = []
        hiperimpulsores = []
        MGLT = []
        velocidades = []
        costo_creditos = []
        
        for nave in self.lista_naves:
            nombres.append(nave.nombre)
            #Se utiliza float para convertir los valores a formato numerico con decimales y poder sacar las cuentas
            if nave.clasificacion_hiperimpulsor == "n/a":
                nave.clasificacion_hiperimpulsor = 0
            hiperimpulsores.append(float(nave.clasificacion_hiperimpulsor))
            if nave.MGLT == "n/a":
                nave.MGLT = 0
            MGLT.append(float(nave.MGLT))
            if nave.velocidad_maxima_atmosfera == "n/a":
                nave.velocidad_maxima_atmosfera = 0
            #Se leen los ultimos 2 caracteres del string para verificar si incluyen "km" como unidad de medida
            else:
                if nave.velocidad_maxima_atmosfera[-2:] == "km":
                #De incluir "km" al final del string, se eliminan dichos caracteres para obtener solo el valor numerico y poder realizar los calculos
                    nave.velocidad_maxima_atmosfera = nave.velocidad_maxima_atmosfera[:-2]
            velocidades.append(float(nave.velocidad_maxima_atmosfera))
            if nave.costo == "n/a" or nave.costo == "unknown":
                nave.costo = 0
            costo_creditos.append(float(nave.costo))
            
        data = {
        'Nombre de nave': nombres,
        'Clasificación de hiperimpulsor': hiperimpulsores,
        'MGLT': MGLT,
        'Velocidad máxima en atmósfera': velocidades,
        'Costo (en créditos)': costo_creditos
        }
        
        #Se crea el DataFrame de Pandas
        df = pd.DataFrame(data)
        #Se calculan las estadísticas por cada atributo de las naves
        stats = df.groupby('Nombre de nave').agg({
        'Clasificación de hiperimpulsor': [mean, mode, 'min', 'max'],
        'MGLT': [mean, mode, 'min', 'max'],
        'Velocidad máxima en atmósfera': [mean, mode, 'min', 'max'],
        'Costo (en créditos)': [mean, mode, 'min', 'max']
        })
        #Se le da nombre a las columnas resultantes
        stats.columns = ['Promedio Hiperimpulsor', 'Moda Hiperimpulsor', 'Mínimo Hiperimpulsor', 'Máximo Hiperimpulsor',
        'Promedio MGLT', 'Moda MGLT', 'Mínimo MGLT', 'Máximo MGLT',
        'Promedio Velocidad', 'Moda Velocidad', 'Mínimo Velocidad', 'Máximo Velocidad',
        'Promedio Costo', 'Moda Costo', 'Mínimo Costo', 'Máximo Costo'
        ]
        stats = stats.round(2)
        print(stats)
=======
'''
modulo = moduloNave(response)
for nave in modulo.lista_naves:
    nave.mostrar_nave()
'''
>>>>>>> main
