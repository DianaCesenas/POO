from tkinter import *
from tkinter import ttk


ventana=Tk()
ventana.title("Progressbar")
ventana.geometry("500x500")

def progreso():
    barraprogreso['value']=0
    ventana.update()
    for i in range(1,101):
        barraprogreso['value']=i
        ventana.update()
        ventana.after(30)



barraprogreso=ttk.Progressbar(ventana,mode="determinate",length=200)
barraprogreso.pack()
barraprogreso['value']=0


btn_iniciar=Button(ventana,text="Iniciar progreso", command=progreso)
btn_iniciar.pack()

ventana.mainloop()