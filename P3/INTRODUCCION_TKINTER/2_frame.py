from tkinter import *

ventana=Tk()
ventana.geometry("800x600")
ventana.title("Marcos o frame en tkinter ")
ventana.resizable(False,False) #no pueda modificarse el tamaño de la 

marco1=Frame(ventana,width=600,height=400,bg="red",relief=SOLID, border=2)
marco1.pack_propagate(False) #Evitar que se modifique el estilo del marco 
marco1.pack(pady=50) # es importante para que se dibuje o muestre el objetodentro de la ventana

marco2=Frame(ventana,width=300,height=150,bg="silver",relief=GROOVE, border=10).pack()

ventana=mainloop()