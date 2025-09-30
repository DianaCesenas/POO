#Instanciar los objetos para posteriormente implementarlos

from coches import Coches
import os
os.system("cls")

num_coches = int(input("Cuantos coches deseas crear?"))

for i in range(0, num_coches):

 print(f"\n\t..:Datos del coche: {i + 1}...")
 marca = input("Ingresa la marca: ").upper()
 color = input("Ingresa el color: ").upper()
 modelo = input("Ingresa el modelo: ").upper()
 velocidad = int (input("Ingrese la velocidad: "))
 potencia = int (input("Ingrese la potencia: "))
 plazas = int (input("Ingrese las plazas: "))

 coche1 = Coches(marca, color, modelo, velocidad, potencia, plazas)

print(f"Datos del vehiculo: \nMarca: {coche1.marca} \nColor: {coche1.getColor()} \nModelo{coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()}, \nCaballahje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")

print(f"\n\n\t {coche1.acelerar()}")
"""coche1 = Coches("VW", "Blanco", "2022", 220, 150, 5)
coche2 = Coches("Nissan", "Azul", "2020", 180, 150, 6)
coche3 = Coches("Honda", "", "", 0, 0, 0)


print(f"Datos del vehiculo: \nMarca: {coche1.marca} \nColor: {coche1.getColor()} \nModelo{coche1.getModelo()} \nVelocidad: {coche1.getVelocidad()} \nCaballahje: {coche1.getCaballaje()} \nPlazas: {coche1.getPlazas()}")
"""