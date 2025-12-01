from tkinter import *
import os 

ventana=Tk()
ventana.title("Imagenes con Pillow ")
ventana.geometry("500x500")


def mensaje(tipo):
    resultado.config(text=f"{tipo}")

# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))
print(ruta_base)

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "image/logo_utd.png")
print(ruta_imagen)


#1 forma de agregar imagenes con tkinter 
# PhotoImage solo permite archivos en extencion .png , .gif 

imagen=PhotoImage(file=ruta_imagen)
#imagen=PhotoImage(file="/Users/marysol/Desktop/POO/P2/INTRODUCCION_TKINTER/logo_utd.png")

#incluir o mostrar la imagen 
etiqueta=Label(ventana,image=imagen,text="Somos bufalos ... UTD", compound="top")
etiqueta.pack()

boton=Button(ventana, image=imagen,command=lambda: mensaje("hola python"))
boton.pack()

resultado=Label(ventana,text="")
resultado.pack()



ventana.mainloop()
