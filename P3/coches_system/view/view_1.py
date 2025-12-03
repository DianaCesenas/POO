from tkinter import *

class View:
    def __init__(self,ventana):
        ventana.title("Coches")
        # ventana.geometry("1024x768")
        ventana.geometry("800x400")
        ventana.config(bg="#93a5fb")
        self.menu_principal(ventana)

    
    def borrarPantalla(self,ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def regresar(self,ventana,tipo):
        regresar=Button(ventana,text=("Regresar"), command= lambda: self.menu_acciones(ventana,tipo))
        regresar.pack(pady=10)
    
    def menu_principal(self,ventana):
        self.borrarPantalla(ventana)
        Label(ventana,text="Bienvenido al sistema",font=("Times New Roman", 30),bg="#93a5fb").pack(pady=10)

        autos=Button(ventana,text="Autos",command= lambda: self.menu_acciones(ventana,"Autos"))
        autos.pack(pady=10)

    def menu_acciones(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f" {tipo}",font=("Times New Roman", 25),bg="#93a5fb")
        text.pack(pady=10)
        text= Label(ventana, text=f"Indique la acción que desea realizar:  ",font=("Times New Roman", 15),bg="#93a5fb")
        text.pack(pady=10)
        
        

        inser=Button(ventana, text="Insertar", command= lambda: self.insertar_vehiculos(ventana,tipo))
        inser.pack(pady=10)
        con=Button(ventana, text="Consultar", command= lambda:self.consultar_vehiculos(ventana,tipo))
        con.pack(pady=10)
        cam=Button(ventana, text="Cambiar", command= lambda:self.cambiar_vehiculos(ventana,tipo))
        cam.pack(pady=10)
        eli=Button(ventana, text="Eliminar", command= lambda:self.borrar_vehiculos(ventana,tipo))
        eli.pack(pady=10)
        reg=Button(ventana,text="Regresar", command= lambda: self.menu_principal(ventana))
        reg.pack()

    def insertar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"{tipo}",font=("Times New Roman",25 ),bg="#93a5fb")
        text.pack(pady=10)  
        text= Label(ventana, text=f"Insertar",font=("Times New Roman", 15),bg="#93a5fb")
        text.pack(pady=10) 
        self.regresar(ventana, tipo)      

    def consultar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"{tipo}",font=("Times New Roman",25 ),bg="#93a5fb")
        text.pack(pady=10)  
        text= Label(ventana, text=f"Consultar",font=("Times New Roman", 15),bg="#93a5fb")
        text.pack(pady=10) 
        self.regresar(ventana,tipo)


    def cambiar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"{tipo}",font=("Times New Roman", 30),bg="#93a5fb")
        text.pack(pady=10)

        text= Label(ventana, text=f"Id del vehículo a cambiar:")
        text.pack(pady=10)
        id=IntVar()
        ent=Entry(ventana,textvariable=id)
        ent.pack(pady=10)
        self.regresar(ventana,tipo)

    def borrar_vehiculos(self,ventana,tipo):
        self.borrarPantalla(ventana)
        text= Label(ventana, text=f"Borrar {tipo}",font=("Times New Roman", 30),bg="#93a5fb")
        text.pack(pady=10)

        text= Label(ventana, text=f"Id del vehículo que desea borrar:")
        text.pack(pady=10)
        id=IntVar()
        ent=Entry(ventana,textvariable=id)
        ent.pack(pady=10)
        self.regresar(ventana,tipo)