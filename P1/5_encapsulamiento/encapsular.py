#Encapsular. Es un pilar de la POO que permite indicar cual es la manera de como poder usar los atributos y metodos de una clase a la hora de usar en objetos o en herencia

import os
os.system ("cls")

class Clase:
    atributo_publico="Soy un atributo  publico"
    _atributo_protegido="Soy un atributo protgido"
    __atributo_privado="Soy un atributo privado"
    
    def __init__(self, color, tamano):
        self.__color= color
        self.__tamano = tamano
    
    @property
    def publico(self):
        return self.publico
   
    @publico.setter
    def publico(self, publico):
        self.publico= publico
################################################################
    @property
    def atributo_protegido(self):
        return self._atributo_protegido
   
    @atributo_protegido.setter
    def atributo_protegido(self, atributo_protegido):
        self._atributo_protegido= atributo_protegido
###################################################################3
    @property
    def atributo_privado(self):
        return self.__atributo_privado
   
    @atributo_privado.setter
    def atributo_privado(self, atributo_privado):
        self.__atributo_privado= atributo_privado
#######################################################
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color = color
#################################33
    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(self,tamano):
        self.tamano = tamano

#############################################
    def getAtributoPrivado(self):
        return self.__atributo_privado

#Utilizar la clase

objeto = Clase("Rosa", "Mediano")
#print(objeto.atributo_publico) No es una buena practica acceder a los atributos directamente
#print(objeto._atributo_protegido)
print(objeto.publico)
print(objeto.atributo_protegido)
print(objeto.atributo_privado)
objeto.color="amarillo"
print(objeto)
