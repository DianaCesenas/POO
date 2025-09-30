import os
os.system("cls")

class Coches:
   
   #metodo constructor, con este metodo se inicializa un objeto cuando es creado con valores inicales

    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas): #Este es dinamico, se adapta a los valores que ingresas
   
     self.__marca = marca
     self.__color = color
     self.__modelo = modelo 
     self.__velocidad = velocidad
     self.__caballaje = caballaje
     self.__plazas = plazas

 #Crear los metodos getter y seter. Estos metodos son importantes y necesarios en todas las clases para que el programador interactue con los valores de los atributos a traves de estos metodos.. digamos que es la manera mas adecuada  y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor(set) a un atributo en particular de la clase a traves de un objeto
    #En teoria se deberia de crear un metodo getters y setters para cada atributo que contenga la clase
    #los metodos ger siempre regresan valor, es decir el valor de la propiedad a traves del return
    #Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

    #1er forma de crear get y set
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca

    #2da forma
    @property
    def marca(self):
        return self.__marca #metodo set
    
    @marca.setter
    def marca(self,marca):
        self.__marca=marca
##################################################
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo = modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self, velocidad):
        self.__velocidad = velocidad

    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self, caballaje):
        self.__caballaje = caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self, plazas):
        self.__plazas = plazas
    
    
    def acelerar(self):
        pass
        
    
    def frenar(self):
        pass
#Fin definir clase

#Crear objetos o instanciar clases

#Multiples objetos
coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3 = Coches("Honda", "", "", 0, 0, 0)


print(f"Datos del vehiculo: \nMarca: {coche1.marca} \nColor: {coche1.getColor()} \nModelo{coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()}, \nCaballahje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")
