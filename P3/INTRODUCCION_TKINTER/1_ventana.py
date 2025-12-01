"""
Tkinter trabaja a traves de interfaces, es una biblioteca de python que permite 
cear aplicaciones en python para escritorio
"""

#import tkinter as tk
#ventana=tk.Tk()
from tkinter import *

ventana=Tk()
ventana.title("Mi primer app con tkinter")
ventana.geometry("800x600")
ventana.mainloop() #metodo que permite tener la ventana abierta todo el tiempo que dure la app activa 