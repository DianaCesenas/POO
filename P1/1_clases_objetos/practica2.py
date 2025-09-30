"""

Ejercicio Practico #2: "Modelar y Diagramar en POO"

"""

import os
os.system("cls")

#Clase de coches #el self, se puede reemplazar por otras palabras, como "hola", esta palabra se usa para que el atributo sea reconocible dentro de otros metodos de la clase  
class Coches:
    def __init__(self, color, marca, velocidad):#metodo constructor que inicializa los valoree cuando se instancia un objeto de la clase
        self.__color = color #Atributos del objeto #con un doble guion bajo python hace un atributo privado. Protegido se representa con un solo _
        self.__marca = marca
        self.__velocidad = velocidad

    #Metodos del objeto
    def acelerar(self, incremento):
        self.__velocidad = self.__velocidad + incremento
        return self.__velocidad
    
    def frenar(self, decremento):
        self.__velocidad = self.__velocidad - decremento 
        return self.__velocidad
    
    def tocar_claxon(self):
        print("pIIIIIIIIIIIIp")
    
#Instanciar o crear objetos de la clase coches
coche1 = Coches("Blanco", "Toyota", 220)
coche2 = Coches("Amarillo", "Nissan", 180)

print(coche1.tocar_claxon())
print(coche1.acelerar(59))
print(coche2.frenar(100))
#print(f"Los valores del objeto 1 son: {coche1.__marca}, {coche1.__color}, {coche1.__velocidad}") #acceder a ;os atributos atravez de metodos
#print(f"El coche 1 acelero de: {coche1.__velocidad} a {coche1.acelerar(50)}")
#print(f"Los valores del objeto 1 son: {coche2.__marca}, {coche2.__color}, {coche2.__velocidad}")
#print(f"El coche 2 freno de: {coche2.__velocidad} a {coche2.frenar(100)}")

#Pueden haber clases sin constructores. Hacerlo privado significa que los valores van a cambiar