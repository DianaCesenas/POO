from tkinter import *
from tkinter import messagebox

def suma(numero1,numero2):
    suma=numero1+numero2
    messagebox.showinfo(icon="info", title="Suma", message=F"{numero1} + {numero2} = {suma}")

def resta(numero1,numero2):
    resta=numero1-numero2
    messagebox.showinfo(icon="info", title="Resta", message=F"{numero1} - {numero2} = {resta}")

def multiplicacion(numero1,numero2):
    multiplicacion=numero1*numero2
    messagebox.showinfo(icon="info", title="Multiplicacion", message=F"{numero1} * {numero2} = {multiplicacion}")

def division(numero1,numero2):
    division=numero1/numero2
    messagebox.showinfo(icon="info", title="Division ", message=F"{numero1} / {numero2} = {division}")


def operaciones(titulo,numero1,numero2,signo):
    if signo=="+":
        resultado=numero1+numero2
    elif signo=="-":
        resultado=numero1-numero2
    elif signo=="x":
        resultado=numero1*numero2
    elif signo=="/":
        resultado=numero1/numero2
    messagebox.showinfo(icon="info",title=titulo,message=f"{numero1}+{numero2}={resultado}")