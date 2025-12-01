from tkinter import *

ventana=Tk()
ventana.title("Menu ")
ventana.geometry("500x500")

def mostrarEstado(tipo):
    resultado.config(text=f"{tipo}")

menuBar=Menu(ventana)
ventana.config(menu=menuBar)

archivoMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo archivo", command=lambda: mostrarEstado("Nuevo archivo"))
archivoMenu.add_command(label="Guardar archivo", command=lambda: mostrarEstado("Guardar archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventana.quit)


edicionMenu=Menu(menuBar,tearoff=False)
menuBar.add_cascade(label="Edicion", menu=edicionMenu)
edicionMenu.add_command(label="Copiar", command=lambda: mostrarEstado("Copiar"))
edicionMenu.add_command(label="Recortar", command=lambda: mostrarEstado("Rocordadar"))
edicionMenu.add_separator()
edicionMenu.add_command(label="Salir", command=ventana.quit)


resultado=Label(ventana,text="")
resultado.pack()

ventana.mainloop()