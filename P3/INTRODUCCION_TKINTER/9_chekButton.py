from tkinter import *

ventana=Tk()
ventana.title("chek Button")
ventana.geometry("500x500")

def mostrarEstado():
    if opcion.get()==1:
        resultado.config(text="Notificaciones Activadas")
    else:
        resultado.config(text="Notificaciones Desactivadas")

opcion=IntVar()
checkbutton=Checkbutton(ventana,text="Deseas recibir notificaciones?",variable=opcion,
                        onvalue=1,offvalue=0)
checkbutton.pack()

boton=Button(ventana, text="Confirmar", command=mostrarEstado )
boton.pack(pady=10)

resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()