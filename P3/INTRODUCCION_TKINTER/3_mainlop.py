from tkinter import *

ventana=Tk()
ventana.geometry("600x400")
ventana.title("Uso del mainlop ")

marco1=Frame(ventana, width=600,height=50,bg="#FF0202",border=2,relief="raised").pack()
marco2=Frame(ventana, width=600,height=50,bg="#FF5B02",border=2,relief="raised").pack()
marco3=Frame(ventana, width=600,height=50,bg="#FFD902",border=2,relief="raised").pack()
marco4=Frame(ventana, width=600,height=50,bg="#7CFF02",border=2,relief="raised").pack()
marco5=Frame(ventana, width=600,height=50,bg="#029AFF",border=2,relief="raised").pack()
marco6=Frame(ventana, width=600,height=50,bg="#8902FF",border=2,relief="raised").pack()
ventana=mainloop()