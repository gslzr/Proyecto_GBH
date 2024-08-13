import requests
import pandas as pd

import matplotlib.pyplot as plt
import csv
from statistics import mean, mode
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
                                         info["result"]["properties"]["starship_class"], 
                                        info["result"]["properties"]["length"],
                                        info["result"]["properties"]["cargo_capacity"],
                                        info["result"]["properties"]["hyperdrive_rating"],
                                        info["result"]["properties"]["MGLT"],
                                        info["result"]["properties"]["max_atmosphering_speed"],
                                        info["result"]["properties"]["cost_in_credits"],
                                        lista_pilotos
                                        ))
            


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

    def generar_tabla_mglt(self):
        clases = []
        MGLT = []
        for nave in self.lista_naves:
            clases.append(nave.clase)
            #Se reemplazan los "n/a" por 0 para poder realizar los calculos numericos
            if nave.MGLT == "n/a":
                nave.MGLT = 0
            #Se convierte el MGLT a formato float (numerico con decimales) para poder realizar los calculos y se agregan a una lista    
            MGLT.append(float(nave.MGLT))

        #Se crea el dataframe de pandas con las listas creadas anteriormente
        df = pd.DataFrame({
            'Clase': clases,
            'MGLT': MGLT
        })

        #Se agrupa por clase y se calculan las estadísticas
        tabla_estadisticas = df.groupby('Clase')['MGLT'].agg(['mean', 'max', 'min']).reset_index()
        tabla_estadisticas['moda'] = df.groupby('Clase')['MGLT'].apply(lambda x: x.mode()[0]).values

        #Se renombran las columnas para mayor claridad
        tabla_estadisticas.columns = ['Clase', 'Promedio MGLT', 'Máximo MGLT', 'Mínimo MGLT', 'Moda MGLT']

        print(tabla_estadisticas)

    def generar_tabla_hiperimpulsor(self):
        clases = []
        hiperimpulsores = []
        for nave in self.lista_naves:
            clases.append(nave.clase)
            #Se reemplazan los "n/a" por 0 para poder realizar los calculos numericos
            if nave.clasificacion_hiperimpulsor == "n/a":
                nave.clasificacion_hiperimpulsor = 0
            #Se convierte el MGLT a formato float (numerico con decimales) para poder realizar los calculos y se agregan a una lista    
            hiperimpulsores.append(float(nave.clasificacion_hiperimpulsor))

        #Se crea el dataframe de pandas con las listas creadas anteriormente
        df = pd.DataFrame({
            'Clase': clases,
            'Clasificacion Hiperimpulsor': hiperimpulsores
        })

        #Se agrupa por clase y se calculan las estadísticas
        tabla_estadisticas = df.groupby('Clase')['Capacidad Hiperimpulsor'].agg(['mean', 'max', 'min']).reset_index()
        tabla_estadisticas['moda'] = df.groupby('Clase')['Capacidad Hiperimpulsor'].apply(lambda x: x.mode()[0]).values

        #Se renombran las columnas para mayor claridad
        tabla_estadisticas.columns = ['Clase', 'Promedio Hiperimpulsor', 'Máximo Hiperimpulsor', 'Mínimo Hiperimpulsor', 'Moda Hiperimpulsor']

        print(tabla_estadisticas)

    def generar_tabla_velocidad(self):
        clases = []
        velocidades = []
        for nave in self.lista_naves:
            #Se reemplazan los n/a por cero para poder realizar los calculos
            if nave.velocidad_maxima_atmosfera == "n/a":
                nave.velocidad_maxima_atmosfera = 0
            #Se leen los ultimos 2 caracteres del string para verificar si incluyen "km" como unidad de medida
            else:
                if nave.velocidad_maxima_atmosfera[-2:] == "km":
                #De incluir "km" al final del string, se eliminan dichos caracteres para obtener solo el valor numerico y poder realizar los calculos
                    nave.velocidad_maxima_atmosfera = nave.velocidad_maxima_atmosfera[:-2]
            velocidades.append(float(nave.velocidad_maxima_atmosfera))
        #Se crea el dataframe de pandas con las listas creadas anteriormente
        df = pd.DataFrame({
            'Clase': clases,
            'Velocidad max atmosfera': velocidades
        })

        #Se agrupa por clase y se calculan las estadísticas
        tabla_estadisticas = df.groupby('Clase')['Velocidad max atmosfera'].agg(['mean', 'max', 'min']).reset_index()
        tabla_estadisticas['moda'] = df.groupby('Clase')['Velocidad max atmosfera'].apply(lambda x: x.mode()[0]).values

        #Se renombran las columnas para mayor claridad
        tabla_estadisticas.columns = ['Clase', 'Promedio Velocidades', 'Máximo Velocidades', 'Mínimo Velocidades', 'Moda Velocidades']

        print(tabla_estadisticas)

    def generar_tabla_costo(self):
        clases = []
        costos_creditos = []
        for nave in self.lista_naves:
            #Se reemplazan los n/a por cero para poder realizar los calculos
            if nave.costo == "n/a" or nave.costo == "unknown":
                nave.costo = 0
            costos_creditos.append(float(nave.costo))
        #Se crea el dataframe de pandas con las listas creadas anteriormente
        df = pd.DataFrame({
            'Clase': clases,
            'Costo en Creditos': costos_creditos
        })

        #Se agrupa por clase y se calculan las estadísticas
        tabla_estadisticas = df.groupby('Clase')['Costo en Creditos'].agg(['mean', 'max', 'min']).reset_index()
        tabla_estadisticas['moda'] = df.groupby('Clase')['Costo en Creditos'].apply(lambda x: x.mode()[0]).values

        #Se renombran las columnas para mayor claridad
        tabla_estadisticas.columns = ['Clase', 'Promedio Costos', 'Máximo Costos', 'Mínimo Costos', 'Moda Costos']

        print(tabla_estadisticas)
