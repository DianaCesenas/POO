from tkinter import *

"""
def cambiar():
    lbl_resultado.config(text=f"Bienvenido..{nombre.get()}")

ventana=Tk()
ventana.title("Entry")
ventana.geometry("500x500")

lbl_nombre=Label(ventana,text="Ingrese su nombre:").pack()

nombre=StringVar()
txt_nombre=Entry(ventana,textvariable=nombre)
txt_nombre.pack()

btn_saludar=Button(ventana,text="Saludar", command=cambiar)
btn_saludar.pack()

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()

ventana.mainloop()

"""

ventana=Tk()
ventana.title("Entry")
ventana.geometry("800x600")

def cambiar():
    lbl_resultado.config(
        text=f"Bienvenido al sistema {nombre.get()}",
        bg="lightblue",
        fg="darkblue",
        width=50,
        height=4,
        font=("Helvetica",30,"italic"),
        relief=SOLID,
        border=2
        )
    
def borrar():
    txt_nombre.delete(0,END)
    txt_password.delete(0,END)
    txt_nombre.focus()
    lbl_resultado.destroy()
    #color_defecto=ventana.cget("bg")
    #lbl_resultado.config(
      #  text='',
       # bg=color_defecto,
        #border=0
    #)

def salir():
    ventana.quit()

etiqueta=Label(ventana,text="Acceso al sistema")
etiqueta.config(
    bg="lightblue",
    fg="darkblue",
    width=50,
    height=4,
    font=("Helvetica",30,"italic"),
    relief=SOLID,
    border=2
)
etiqueta.pack()

marco=Frame(ventana)
marco.config(
    width=800,
    height=300,
)
marco.pack_propagate(False)
marco.pack()

lbl_nombre=Label(marco,text="Nombre de usuario")
lbl_nombre.grid(row=0,column=0,padx=5,pady=5)

nombre=StringVar()
txt_nombre=Entry(marco,textvariable=nombre)
txt_nombre.focus()
txt_nombre.grid(row=0,column=1,padx=5,pady=5)

lbl_password=Label(marco,text="Contraseña")
lbl_password.grid(row=1,column=0,padx=5,pady=5)

password=StringVar()
txt_password=Entry(marco,textvariable=password,show=".")
txt_password.grid(row=1,column=1,padx=5,pady=5)

marco_botones=Frame(ventana)
marco_botones.config(
    width=800,
    height=300,
)
marco_botones.pack_propagate(False)
marco_botones.pack()

btn_entrar=Button(marco_botones,text="Entrar", command=cambiar)
btn_entrar.grid(row=0,column=0,padx=5,pady=5)

btn_borrar=Button(marco_botones,text="Borrar", command=borrar)
btn_borrar.grid(row=0,column=1,padx=5,pady=5)

btn_salir=Button(marco_botones,text="Salir",command=salir)
btn_salir.grid(row=0,column=2,padx=5,pady=5)


"""
lbl_nombre=Label(ventana,text="Nombre de usuario").pack()

nombre=StringVar()
txt_nombre=Entry(ventana,textvariable=nombre)
txt_nombre.focus()
txt_nombre.pack()

lbl_password=Label(ventana,text="Contraseña").pack()

password=StringVar()
txt_password=Entry(ventana,textvariable=password,show=".")
txt_password.focus()
txt_password.pack()

btn_entrar=Button(ventana,text="Entrar", command=cambiar)
btn_entrar.pack()

btn_borrar=Button(ventana,text="Borrar", command=borrar)
btn_borrar.pack()

btn_salir=Button(ventana,text="Salir",command=salir)
btn_salir.pack()

"""

lbl_resultado=Label(ventana,text="")
lbl_resultado.pack()

ventana.mainloop()
