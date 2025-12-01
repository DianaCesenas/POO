from tkinter import *

ventana=Tk()
ventana.title("Radio Button")
ventana.geometry("500x500")

def mostrarEstado():
    resultado.config(text=f"Opcion selecionada {opcion.get()}")

opcion=StringVar()
radioBoton1=Radiobutton(ventana,text="Opcion 1",variable=opcion,value="Opcion1")
radioBoton1.pack()

radioBoton2=Radiobutton(ventana,text="Opcion 2",variable=opcion,value="Opcion2")
radioBoton2.pack()

radioBoton3=Radiobutton(ventana,text="Opcion 3",variable=opcion,value="Opcion3")
radioBoton3.pack()


boton=Button(ventana, text="Mostrar Opcion ", command=mostrarEstado )
boton.pack(pady=10)

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()