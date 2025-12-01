from tkinter import *

ventana=Tk()
ventana.title("Scale")
ventana.geometry("500x500")

def mostrarEstado():
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()}")

valor=IntVar()
escala=Scale(ventana, from_=0,to=100,orient="horizontal",variable=valor)
escala.pack()


boton=Button(ventana, text="Mostrar valor ", command=mostrarEstado )
boton.pack(pady=10)

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()