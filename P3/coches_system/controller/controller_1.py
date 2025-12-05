from tkinter import messagebox
from model import cochesBD

class Controlador:

    @staticmethod
    def insertar(tipo, *args):
        resultado = False
        if tipo == "Autos":
            resultado = cochesBD.Autos.insertar(*args)
        elif tipo == "Camiones":
            resultado = cochesBD.Camiones.insertar(*args)
        elif tipo == "Camionetas":
            resultado = cochesBD.Camionetas.insertar(*args)
        
        Controlador.respuesta_sql("Insertar", resultado)

    @staticmethod
    def consultar(tipo):
        if tipo == "Autos":
            return cochesBD.Autos.consultar()
        elif tipo == "Camiones":
            return cochesBD.Camiones.consultar()
        elif tipo == "Camionetas":
            return cochesBD.Camionetas.consultar()
        return []

    @staticmethod
    def buscar_por_id(tipo, id):
        if tipo == "Autos":
            return cochesBD.Autos.buscar(id)
        elif tipo == "Camiones":
            return cochesBD.Camiones.buscar(id)
        elif tipo == "Camionetas":
            return cochesBD.Camionetas.buscar(id)
        return None

    @staticmethod
    def actualizar(tipo, *args):
        resultado = False
        if tipo == "Autos":
            resultado = cochesBD.Autos.actualizar(*args)
        elif tipo == "Camiones":
            resultado = cochesBD.Camiones.actualizar(*args)
        elif tipo == "Camionetas":
            resultado = cochesBD.Camionetas.actualizar(*args)
            
        Controlador.respuesta_sql("Actualizar", resultado)

    @staticmethod
    def eliminar(tipo, id):
        resultado = False
        if tipo == "Autos":
            resultado = cochesBD.Autos.eliminar(id)
        elif tipo == "Camiones":
            resultado = cochesBD.Camiones.eliminar(id)
        elif tipo == "Camionetas":
            resultado = cochesBD.Camionetas.eliminar(id)
            
        Controlador.respuesta_sql("Eliminar", resultado)

    @staticmethod
    def respuesta_sql(titulo, respuesta):
        if respuesta:
            messagebox.showinfo(title=titulo, message="Acción realizada exitosamente")
        else:
            messagebox.showwarning(title=titulo, message="Fallo al realizar la acción")