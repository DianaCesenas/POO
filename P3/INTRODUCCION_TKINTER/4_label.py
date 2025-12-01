from tkinter import *

ventana=Tk()
ventana.geometry("600x400")
ventana.title("Uso del lable")

marco1=Frame(ventana, width=600, height=50, bg="#0099FF", border=2,relief="raised")
marco1.pack_propagate(False)
marco1.pack()
marco2=Frame(ventana, width=600, height=50, bg="#2FA8F9", border=2,relief="raised")
marco2.pack_propagate(False)
marco2.pack()
marco3=Frame(ventana, width=600, height=50, bg="#258ED5", border=2,relief="raised")
marco3.pack_propagate(False)
marco3.pack()
marco4=Frame(ventana, width=600, height=50, bg="#54BAFF", border=2,relief="raised")
marco4.pack_propagate(False)
marco4.pack()

#etiquetas 
etiqueta1=Label(marco1,text="Marysol Aguilera Guzman ", bg="#0099FF").pack(pady=10)
etiqueta2=Label(marco2,text="Universidad Tecnologica De Durango", bg="#2FA8F9").pack(pady=10)
etiqueta3=Label(marco3,text="Tecnologias de la informacion", bg="#258ED5").pack(pady=10)
etiqueta4=Label(marco4,text="Desarrollo de software y multiplataforma ", bg="#54BAFF").pack(pady=10)

ventana.mainloop()

"""
que tenga 4 etiquetas 4 marcos 
"""