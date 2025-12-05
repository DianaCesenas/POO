from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from controller import controller_1

class View:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Coches")
        self.ventana.geometry("900x600")
        self.ventana.config(bg="#93a5fb")
        self.menu_principal(ventana)

    def borrarPantalla(self, ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    def salir(self, ventana):
        ventana.destroy()

    def regresar(self, ventana, tipo):
        Button(ventana, text="Regresar", command=lambda: self.menu_acciones(ventana, tipo)).pack(pady=10)

    def menu_principal(self, ventana):
        self.borrarPantalla(ventana)
        Label(ventana, text="Bienvenido al Sistema", font=("Arial", 25, "bold"), bg="#93a5fb").pack(pady=20)
        
        Button(ventana, text="Autos", width=20, command=lambda: self.menu_acciones(ventana, "Autos")).pack(pady=10)
        Button(ventana, text="Camionetas", width=20, command=lambda: self.menu_acciones(ventana, "Camionetas")).pack(pady=10)
        Button(ventana, text="Camiones", width=20, command=lambda: self.menu_acciones(ventana, "Camiones")).pack(pady=10)
        Button(ventana, text="Salir", width=20, bg="red", fg="white", command=lambda: self.salir(ventana)).pack(pady=20)

    def menu_acciones(self, ventana, tipo):
        self.borrarPantalla(ventana)
        Label(ventana, text=f"Gestión de {tipo}", font=("Arial", 20), bg="#93a5fb").pack(pady=10)
        
        Button(ventana, text="Insertar", width=20, command=lambda: self.insertar_vehiculos(ventana, tipo)).pack(pady=5)
        Button(ventana, text="Consultar", width=20, command=lambda: self.consultar_vehiculos(ventana, tipo)).pack(pady=5)
        Button(ventana, text="Actualizar", width=20, command=lambda: self.cambiar_vehiculos(ventana, tipo)).pack(pady=5)
        Button(ventana, text="Eliminar", width=20, command=lambda: self.borrar_vehiculos(ventana, tipo)).pack(pady=5)
        
        Button(ventana, text="Regresar al Inicio", command=lambda: self.menu_principal(ventana)).pack(pady=20)

   
    def insertar_vehiculos(self, ventana, tipo):
        self.borrarPantalla(ventana)
        Label(ventana, text=f"Insertar {tipo}", font=("Arial", 18), bg="#93a5fb").pack(pady=10)

        marca = StringVar()
        color = StringVar()
        modelo = StringVar()
        velocidad = IntVar()
        caballaje = IntVar()
        plazas = IntVar()
        eje = IntVar()
        capacidadCarga = IntVar()
        traccion = StringVar()
        cerrada = StringVar()

        frame = Frame(ventana, bg="#93a5fb")
        frame.pack()

        self._crear_entrada(frame, "Marca:", marca)
        self._crear_entrada(frame, "Color:", color)
        self._crear_entrada(frame, "Modelo:", modelo)
        self._crear_entrada(frame, "Velocidad:", velocidad)
        self._crear_entrada(frame, "Caballaje:", caballaje)
        self._crear_entrada(frame, "Plazas:", plazas)

        if tipo == "Camiones":
            self._crear_entrada(frame, "Ejes:", eje)
            self._crear_entrada(frame, "Capacidad Carga:", capacidadCarga)
            cmd = lambda: controller_1.Controlador.insertar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), eje.get(), capacidadCarga.get())
        elif tipo == "Camionetas":
            self._crear_entrada(frame, "Tracción:", traccion)
            self._crear_entrada(frame, "Cerrada (Si/No):", cerrada)
            cmd = lambda: controller_1.Controlador.insertar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), traccion.get(), cerrada.get())
        else:
            cmd = lambda: controller_1.Controlador.insertar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get())

        Button(ventana, text="Guardar", bg="green", fg="white", command=cmd).pack(pady=15)
        self.regresar(ventana, tipo)

    def _crear_entrada(self, parent, texto, variable, state='normal'):
        f = Frame(parent, bg="#93a5fb")
        f.pack(pady=2)
        Label(f, text=texto, width=15, anchor="e", bg="#93a5fb").pack(side=LEFT)
        Entry(f, textvariable=variable, state=state).pack(side=LEFT)

    def consultar_vehiculos(self, ventana, tipo):
        self.borrarPantalla(ventana)
        Label(ventana, text=f"Consulta de {tipo}", font=("Arial", 18), bg="#93a5fb").pack(pady=10)

        registros = controller_1.Controlador.consultar(tipo)
        cols = ("ID", "Marca", "Color", "Modelo", "Velocidad", "Caballaje", "Plazas")
        if tipo == "Camiones":
            cols += ("Ejes", "Carga")
        elif tipo == "Camionetas":
            cols += ("Tracción", "Cerrada")

        tree = ttk.Treeview(ventana, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
            tree.column(col, width=90, anchor="center")
        
        tree.pack(fill=BOTH, expand=True, padx=20)
        for row in registros:
            tree.insert("", END, values=row)

        self.regresar(ventana, tipo)

 
    def cambiar_vehiculos(self, ventana, tipo):
        self.borrarPantalla(ventana)
        Label(ventana, text=f"Actualizar {tipo}", font=("Arial", 18), bg="#93a5fb").pack(pady=5)
        
     
        f_buscar = Frame(ventana, bg="#93a5fb")
        f_buscar.pack(pady=10)
        Label(f_buscar, text="Ingrese ID a modificar:", bg="#93a5fb").pack(side=LEFT)
        id_busq = IntVar()
        Entry(f_buscar, textvariable=id_busq, width=10).pack(side=LEFT, padx=5)
        
 
        def buscar_y_mostrar():
            id_val = id_busq.get()
            datos = controller_1.Controlador.buscar_por_id(tipo, id_val)
            
            if datos:
              
                f_buscar.destroy()
                
              
                marca = StringVar(value=datos[1])
                color = StringVar(value=datos[2])
                modelo = StringVar(value=datos[3])
                velocidad = IntVar(value=datos[4])
                caballaje = IntVar(value=datos[5])
                plazas = IntVar(value=datos[6])
                
                eje = IntVar()
                capacidadCarga = IntVar()
                traccion = StringVar()
                cerrada = StringVar()

                
                Label(ventana, text=f"Editando ID: {id_val}", font=("Arial", 12, "bold"), bg="#93a5fb").pack()
                
                frame_form = Frame(ventana, bg="#93a5fb")
                frame_form.pack()
                
                self._crear_entrada(frame_form, "Marca:", marca)
                self._crear_entrada(frame_form, "Color:", color)
                self._crear_entrada(frame_form, "Modelo:", modelo)
                self._crear_entrada(frame_form, "Velocidad:", velocidad)
                self._crear_entrada(frame_form, "Caballaje:", caballaje)
                self._crear_entrada(frame_form, "Plazas:", plazas)

                cmd = None
                if tipo == "Camiones":
                    eje.set(datos[7])
                    capacidadCarga.set(datos[8])
                    self._crear_entrada(frame_form, "Ejes:", eje)
                    self._crear_entrada(frame_form, "Carga:", capacidadCarga)
                    cmd = lambda: controller_1.Controlador.actualizar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), eje.get(), capacidadCarga.get(), id_val)
                elif tipo == "Camionetas":
                    traccion.set(datos[7])
                    cerrada.set(datos[8])
                    self._crear_entrada(frame_form, "Tracción:", traccion)
                    self._crear_entrada(frame_form, "Cerrada:", cerrada)
                    cmd = lambda: controller_1.Controlador.actualizar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), traccion.get(), cerrada.get(), id_val)
                else:
                    cmd = lambda: controller_1.Controlador.actualizar(tipo, marca.get(), color.get(), modelo.get(), velocidad.get(), caballaje.get(), plazas.get(), id_val)

                Button(ventana, text="Guardar Cambios", bg="orange", fg="white", command=cmd).pack(pady=15)
                
            else:
                messagebox.showerror("Error", "ID no encontrado")

        Button(f_buscar, text="Buscar", command=buscar_y_mostrar).pack(side=LEFT)
        self.regresar(ventana, tipo)

  
    def borrar_vehiculos(self, ventana, tipo):
        self.borrarPantalla(ventana)
        Label(ventana, text=f"Eliminar {tipo}", font=("Arial", 18), bg="#93a5fb").pack(pady=20)

        f_buscar = Frame(ventana, bg="#93a5fb")
        f_buscar.pack()
        Label(f_buscar, text="ID a eliminar:", bg="#93a5fb").pack(side=LEFT)
        id_busq = IntVar()
        Entry(f_buscar, textvariable=id_busq).pack(side=LEFT, padx=5)

        def verificar_y_eliminar():
            id_val = id_busq.get()
            datos = controller_1.Controlador.buscar_por_id(tipo, id_val)
            
            if datos:
              
                f_buscar.destroy()
                Label(ventana, text=f"¿Seguro que deseas eliminar este registro?", fg="red", bg="#93a5fb", font=("Arial", 14)).pack(pady=10)
                
                f_datos = Frame(ventana, bg="#93a5fb")
                f_datos.pack()
                
              
                Label(f_datos, text=f"ID: {datos[0]}", bg="#93a5fb").pack()
                Label(f_datos, text=f"Marca: {datos[1]}", bg="#93a5fb").pack()
                Label(f_datos, text=f"Modelo: {datos[3]}", bg="#93a5fb").pack()
                
                Button(ventana, text="CONFIRMAR ELIMINAR", bg="red", fg="white", command=lambda: controller_1.Controlador.eliminar(tipo, id_val)).pack(pady=20)
            else:
                messagebox.showerror("Error", "ID no encontrado")

        Button(f_buscar, text="Buscar", command=verificar_y_eliminar).pack(side=LEFT)
        self.regresar(ventana, tipo)