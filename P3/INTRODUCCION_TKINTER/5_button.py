from tkinter import *


def cambiarTexto():
    lable_nombre.config(text="Marysol Aguilera")
    lable_password.config(text="1234")

def regresarTexto():
    lable_nombre.config(text="Nombre:...")
    lable_password.config(text="Contraseña:...")

ventana=Tk()

ventana.title("Uso de botones, Marcos, Etiquetas")
ventana.geometry("800x600")

marco1=Frame(ventana, width=800, height=100, border=2 ,relief= SOLID, bg="#FE4C4C")
marco1.config(
    width=800, 
    height=100, 
    border=2 ,
    relief= SOLID, 
    bg="#4CCCFE"

)
marco1.pack_propagate(False)
marco1.pack(pady=10)

lable_titulo=Label(marco1,text="Inicio de sesion")
lable_titulo.config(
    bg="#4CCCFE",
    height=10,
    font="Arial"
)
lable_titulo.pack()

lable_nombre=Label(ventana,text="Nombre:...")
lable_nombre.pack(pady=10)
lable_password=Label(ventana,text="Contraseña:...")
lable_password.pack(pady=10)

boton_aceptar=Button(ventana, text="Aceptar", command=cambiarTexto ).pack(pady=10)
boton_regrear=Button(ventana, text="Regresar", command=regresarTexto).pack(pady=10)

ventana.mainloop()