import os
os.system ("cls")

#Clase 1. Alumnos
#Constructor
class Alumnos:
    def __init__(self, nombre, edad, matricula):
        self.__nombre = nombre 
        self.__edad = edad
        self.__matricula = matricula

    #######Getters y Setters
    #Nombre
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad
    
    def setEdad(self, edad):
        self.__edad = edad
 
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
 
 #Metodos
    
    def inscribirse(self):
        return "El alumno se ha inscrito exitosamente"
 
    def estudiar(self):
        return "Estudiando...."
 
 #crear objeto

alumno1 = Alumnos("Diana", 26, 123456789)
alumno2 = Alumnos("Laura", 26, 323456789)

print(f"El alumno1 es: \nNombre: {alumno1.getNombre()} \nEdad: {alumno1.getEdad()} \nMatricula{alumno1.getMatricula()}")

#########################################################################################################################3
class Profesores:
    def __init__(self, nombre, experiencia, num_profesor):
        self.__nombre = nombre 
        self.__experiencia = experiencia
        self.__num_profesor = num_profesor

    #######Getters y Setters
    #Nombre
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getExperiencia(self):
        return self.__experiencia
    
    def setExperiencia(self, experiencia):
        self.__experiencia = experiencia
 
    def getNum_profesor(self):
        return self.__num_profesor
    
    def setNum_profesor(self, num_profesor):
        self.__num_profesor = num_profesor
 
 #Metodos
    
    def imparte(self):
        print("El profesor imparte")
    def evaluar(self):
        print("El profesor evalua")
 
 
 #crear objeto

profesor1 = Profesores("Dago", 26, 123456789)
profesor2 = Profesores("Ana", 3, 123456789)
###############################################################################################
class Curso:
    def __init__(self, nombre, codigo, creditos):
        self.__nombre = nombre 
        self.__codigo = codigo
        self.__creditos = creditos

    #######Getters y Setters
    #Nombre
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getCodigo(self):
        return self.__codigo
    
    def setCodigo(self, codigo):
        self.__codigo = codigo
 
    def getCreditos(self):
        return self.__creditos
    
    def setCreditos(self, creditos):
        self.__creditos = creditos
 
 #Metodos
    
    def asignar(self):
        print("El alumno se ha registrado a ingles")
 
 
 #crear objeto

curso1 = Curso("Ingles", 26, 123456789)
curso2 = Curso("Mate", 26, 123456789)