import pandas as pd

class ModuloMisiones:
    def __init__(self):
        #Se lee cada archivo csv y se crean listas para almacenar los datos a utilizar
        self.personajes = pd.read_csv('characters.csv')
        self.lista_personajes = self.personajes['name'].tolist()

        self.naves = pd.read_csv('starships.csv')
        self.lista_naves = self.naves['name'].tolist()

        self.planetas = pd.read_csv('planets.csv')
        self.lista_planetas = self.planetas['name'].tolist()

        self.armas = pd.read_csv('weapons.csv')
        self.lista_armas = self.armas['name'].tolist()

        self.misiones = []


    def construir_mision(self):
        
        #Se le solicitan los datos al usuario
        print("\nCrear nueva mision: ")
        nombre = input("\nIngrese el nombre de la mision: ")

        planeta = ""
        print("\nLista de planetas: ")
        for i in len(self.lista_planetas):
            #Se usa i-1 porque los indices de las listas empiezan en cero
            print("\n", i, self.lista_planetas[i-1])
        #Se valida que el usuario ingrese un numero valido
        while True:
            planeta_index = input("Seleccione el numero del planeta destino: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_planeta = int(planeta_index)
                
                #Verificar si el número está dentro del rango
                if numero_planeta > 0 and numero_planeta<= len(self.lista_planetas):
                    planeta = self.lista_planetas[numero_planeta-1]
                    break
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.")

        personajes = []
        print("\nLista de personajes: ")
        for i in len(self.lista_personajes):
            #Se usa i-1 porque los indices de las listas empiezan en cero
            print("\n", i, self.lista_personajes[i-1])
        #Mientras no se tengan 7 integrantes de la mision:
        while len(personajes) < 7:
            #Se valida que el usuario ingrese un numero valido
            while True:
                personaje_index = input("Seleccione el numero del personaje que desea incluir: ") 
                try:
                    #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                    numero_personaje = int(personaje_index)
                    
                    #Verificar si el número está dentro del rango
                    if numero_personaje > 0 and numero_personaje<= len(self.lista_personajes):
                        personajes.append(self.lista_personajes[numero_personaje-1])
                    else:
                        print("Por favor, ingrese una opcion valida")
                except ValueError:
                    print("Opcion no válida. Por favor, ingresa un número.")
        
        nave = ""
        print("\nLista de naves: ")
        for i in len(self.lista_naves):
            #Se usa i-1 porque los indices de las listas empiezan en cero
            print("\n", i, self.lista_naves[i-1])
        #Se valida que el usuario ingrese un numero valido
        while True:
            naves_index = input("Seleccione el numero de la nave que desea: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_nave = int(naves_index)
                
                #Verificar si el número está dentro del rango
                if numero_nave > 0 and numero_nave <= len(self.lista_naves):
                    nave = self.lista_naves[numero_nave-1]
                    break
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.")

        armas = []
        print("\nLista de armas: ")
        for i in len(self.lista_armas):
            #Se usa i-1 porque los indices de las listas empiezan en cero
            print("\n", i, self.lista_armas[i-1])
        #Mientras no se tengan 7 integrantes de la mision:
        while len(armas) < 7:
            #Se valida que el usuario ingrese un numero valido
            while True:
                arma_index = input("Seleccione el numero del arma que desea incluir: ") 
                try:
                    #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                    numero_arma = int(arma_index)  
                    
                    #Verificar si el número está dentro del rango
                    if numero_arma > 0 and numero_arma <= len(self.lista_armas):
                        armas.append(self.lista_armas[numero_arma-1])
                        break
                    else:
                        print("Por favor, ingrese una opcion valida")
                except ValueError:
                    print("Opcion no válida. Por favor, ingresa un número.")

        mision = {"Nombre", nombre, "Planeta Destino", planeta, "Nave a utilizar", nave, "Armas a utilizar", armas, "Integrantes de la mision", personajes}
        #Se agrega el diccionario que contiene la mision como una nueva linea del archivo txt 
        archivo = open('misiones.txt', 'a')
        archivo.write(mision)
        #Se guardan los cambios
        archivo.close()

    def cargarMisiones(self):
        with open('misiones.txt', 'r') as archivo:
            #Se leen las líneas y se agregan a la lista misiones
            for linea in archivo:
                if len(self.misiones)<5:
                    self.misiones.append(linea.strip())
                else:
                    print("\nSe ha cargado el maximo de misiones. ")
            print(self.misiones)

    def modificarNombre(self):
        for i in len(self.misiones):
            print("\n", i, self.misiones[i-1])

        #Se valida que el usuario ingrese un numero valido
        while True:
            mision_index = input("\nSeleccione la mision que desea modificar: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_mision = int(mision_index)
                
                #Verificar si el número está dentro del rango
                if numero_mision > 0 and numero_mision<= len(self.misiones):
                    nombre_nuevo = input("Ingrese un nuevo nombre: ")
                    self.misiones[numero_mision]["nombre"] = nombre_nuevo
                    break
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.") 

    def eliminarArmas(self):
        for i in len(self.misiones):
            print("\n", i, self.misiones[i-1])

        #Se valida que el usuario ingrese un numero valido
        while True:
            mision_index = input("\nSeleccione la mision que desea modificar: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_mision = int(mision_index)
                
                #Verificar si el número está dentro del rango
                if numero_mision > 0 and numero_mision<= len(self.misiones):
                    for i in len(self.misiones.armas):
                        print("\n", self.misiones.armas[i-1])
                    while True:
                        arma_index = input("Seleccione el numero del arma que desea eliminar: ") 
                        try:
                            #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                            numero_arma = int(arma_index)  
                            #Verificar si el número está dentro del rango
                            if numero_arma > 0 and numero_arma <= len(self.misiones.armas):
                                #Se utiliza .pop() para eliminar el elemento
                                self.misiones.armas[numero_arma-1].pop()
                                break
                            else:
                                print("Por favor, ingrese una opcion valida")
                        except ValueError:
                            print("Opcion no válida. Por favor, ingresa un número.")
                    arma = input("Seleccione el numero del arma: ")
                    
                    break
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.") 
        
    def AgregarArmas(self):
        for i in len(self.misiones):
            print("\n", i, self.misiones[i-1])

        #Se valida que el usuario ingrese un numero valido
        while True:
            mision_index = input("\nSeleccione la mision que desea modificar: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_mision = int(mision_index)
                
                #Verificar si el número está dentro del rango
                if numero_mision > 0 and numero_mision<= len(self.misiones):
                    if len(self.misiones.armas) < 7:
                        for i in len(self.lista_armas):
                            print("\n", self.lista_armas[i-1])
                        while True:
                            arma_index = input("Seleccione el numero del arma que desea agregar: ") 
                            try:
                                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                                numero_arma = int(arma_index)  
                                #Verificar si el número está dentro del rango
                                if numero_arma > 0 and numero_arma <= len(self.misiones.armas):
                                    self.misiones.armas.append(self.lista_armas[numero_arma-1])
                                    break
                                else:
                                    print("Por favor, ingrese una opcion valida")
                            except ValueError:
                                print("Opcion no válida. Por favor, ingresa un número.")
                        arma = input("Seleccione el numero del arma: ")
                        
                        break
                    else:
                        print("\nYa se ha alcanzado el maximo de armas permitido para una mision. ")
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.") 

    def eliminarPersonaje(self):
        for i in len(self.misiones):
            print("\n", i, self.misiones[i-1])

        #Se valida que el usuario ingrese un numero valido
        while True:
            mision_index = input("\nSeleccione la mision que desea modificar: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_mision = int(mision_index)
                
                #Verificar si el número está dentro del rango
                if numero_mision > 0 and numero_mision<= len(self.misiones):
                    for i in len(self.misiones.personajes):
                        print("\n", self.misiones.personajes[i-1])
                    while True:
                        personaje_index = input("Seleccione el numero del personaje que desea eliminar: ") 
                        try:
                            #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                            numero_personaje = int(personaje_index)  
                            #Verificar si el número está dentro del rango
                            if numero_personaje > 0 and numero_personaje <= len(self.misiones.personajes):
                                #Se utiliza .pop() para eliminar el elemento
                                self.misiones.personajes[numero_personaje-1].pop()
                                break
                            else:
                                print("Por favor, ingrese una opcion valida")
                        except ValueError:
                            print("Opcion no válida. Por favor, ingresa un número.")
                    arma = input("Seleccione el numero del arma: ")
                    
                    break
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.") 

    def AgregarPersonajes(self):
        for i in len(self.misiones):
            print("\n", i, self.misiones[i-1])

        #Se valida que el usuario ingrese un numero valido
        while True:
            mision_index = input("\nSeleccione la mision que desea modificar: ") 
            try:
                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                numero_mision = int(mision_index)
                
                #Verificar si el número está dentro del rango
                if numero_mision > 0 and numero_mision<= len(self.misiones):
                    #Se valida que no se puedan agregar mas de 7 personajes
                    if len(self.misiones.personajes) < 7:
                        for i in len(self.lista_personajes):
                            print("\n", self.lista_personajes[i-1])
                        while True:
                            personaje_index = input("Seleccione el numero del personaje que desea agregar: ") 
                            try:
                                #Se  intenta convertir el valor ingresado por el usuario a valor numerico
                                numero_personaje = int(personaje_index)  
                                #Verificar si el número está dentro del rango
                                if numero_personaje > 0 and numero_personaje <= len(self.misiones.personajes):
                                    self.misiones.personajes.append(self.lista_personajes[numero_personaje-1])
                                    break
                                else:
                                    print("Por favor, ingrese una opcion valida")
                            except ValueError:
                                print("Opcion no válida. Por favor, ingresa un número.")
                        arma = input("Seleccione el numero del arma: ")
                        
                        break
                    else:
                        print("\nYa se ha alcanzado el maximo de armas permitido para una mision. ")
                else:
                    print("Por favor, ingrese una opcion valida")
            except ValueError:
                print("Opcion no válida. Por favor, ingresa un número.") 

    def modificarMision(self):
        while True:
            opcion = input("¿Que accion desea realizar? \n1. Modificar nombre de mision \n2. Agregar arma \n3. Eliminar arma \n4. Agregar personaje \n5. Eliminar Personaje \n6. Salir \n")
            if opcion == "1":
                self.modificarNombre()
            elif opcion =="2":
                self.AgregarArmas()
            elif opcion == "3":
                self.eliminarArmas()
            elif opcion == "4":
                self.AgregarPersonajes()
            elif opcion == "5":
                self.eliminarPersonaje()
            elif opcion == "6":
                break
            else:
                opcion = input("Ingrese una opcion valida: ")
    
    def visualizarMisiones(self):
        for mision in self.misiones:
            print(f"Nombre Mision: {mision['nombre']}, Planeta Destino: {mision['planeta']}, Nave a utilizar: {mision['nave']}, Armas: {mision['armas']}, Personajes: {mision['personajes']}" )


        
    def menuMisiones(self):
        while True:
            opcion = input("Bienvenido a módulo de misiones. ¿Qué acción desea realizar? \n1. Crear nueva misión \n2. Cargar misiones \n3. Modificar misión \n4. Visualizar misión \n5. Salir \n")
            if opcion == "1":
                self.construir_mision()
            elif opcion =="2":
                self.cargarMisiones()
            elif opcion == "3":
                self.modificarMision()
            elif opcion == "4":
                self.visualizarMisiones()
            elif opcion == "5":
                break
            else:
                opcion = input("Ingrese una opcion valida: ")