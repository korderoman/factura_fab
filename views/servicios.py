from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#importamos el controlador
from controllers.datos import *

class Vista_Servicios():
    def __init__(self,aplicacion):
        #creamos una instancia de la bbdd
        self.bbdd=Controlador_BBDD()
        self.mx=5
        self.my=5
        self.ancho=30
        self.aplicacion=aplicacion
        #variables de formulario
        self.var_nuevo_nombre=StringVar()
        self.var_nuevo_unidad=StringVar()
        self.var_nuevo_cu=DoubleVar()
        self.servicio_combobox=None

        self.var_actualizar_id=IntVar()
        self.var_actualizar_nombre=StringVar()
        self.var_actualizar_unidad=StringVar()
        self.var_actualizar_cu=DoubleVar()
        #frames
        self.frame_principal=Frame(self.aplicacion)
        #se implementa la interfaz
        self.interfaz(self.frame_principal)

    def interfaz(self,padre):
        frame_nuevo=LabelFrame(padre,text="Nuevo Registro")
        frame_actualizar=LabelFrame(padre,text="Actualizar o Eliminar Registro")
        #contenido del frame nuevo
        Label(frame_nuevo,text="Nombre del Servicio: ").grid(row=0, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_nombre,width=self.ancho).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_nuevo,text="Unidad: ").grid(row=1, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_unidad,width=self.ancho).grid(row=1,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_nuevo,text="Costo Unitario: ").grid(row=2, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_cu,width=self.ancho).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W)
        Button(frame_nuevo,text="Agregar",command=lambda:self.agregar_servicio()).grid(row=3,column=0,padx=self.mx,pady=self.my, sticky=W+E)
        #contenido del frame actualizar
        self.servicio_combobox=ttk.Combobox(frame_actualizar, state="readonly",width=self.ancho-3)
        self.servicio_combobox["values"]=self.listar_servicios()
        self.servicio_combobox.current(0)
        self.servicio_combobox.grid(row=0,column=0, padx=self.mx,pady=self.my,sticky=W)
        Button(frame_actualizar,text="Buscar",command=lambda:self.obtener_servicio(self.servicio_combobox.get())).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(frame_actualizar,text="Nombre del Servicio: ").grid(row=1, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_nombre,width=self.ancho).grid(row=1,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_actualizar,text="Unidad: ").grid(row=2, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_unidad,width=self.ancho).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_actualizar,text="Costo Unitario: ").grid(row=3, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_cu,width=self.ancho).grid(row=3,column=1,padx=self.mx,pady=self.my,sticky=W)
        Button(frame_actualizar,text="Actualizar",command=lambda:self.actualizar_servicio()).grid(row=4,column=0,padx=self.mx,pady=self.my,sticky=W+E)
        Button(frame_actualizar,text="Eliminar",command=lambda:self.eliminar_servicio()).grid(row=4,column=1,padx=self.mx,pady=self.my,sticky=W+E)

        frame_nuevo.pack(side="left",fill=Y)
        frame_actualizar.pack(side="left",fill=Y)
    
    
    #funciones de procesamiento
    def agregar_servicio(self):
        #print(type(self.var_nuevo_nombre.get()))
        if self.var_nuevo_nombre.get()!="" and self.var_nuevo_unidad.get()!="":
            servicio=[self.var_nuevo_nombre.get(),self.var_nuevo_unidad.get(),self.var_nuevo_cu.get()]
            self.var_nuevo_nombre.set("")
            self.var_nuevo_unidad.set("")
            self.var_nuevo_cu.set(0.0)
            self.bbdd.agregar_servicio(servicio)
            self.servicio_combobox["values"]=self.listar_servicios()
            self.servicio_combobox.current(0)
        else:
            messagebox.showinfo(message="Debe llenar todos los campos",title="Error")

    def listar_servicios(self):
        datos=self.bbdd.obtener_servicios()
        resultados=[]
        for dato in datos:
            resultados.append(dato[0])
        return resultados
    
    def obtener_servicio(self,servicio):
        dato=self.bbdd.obtener_servicio(servicio)
        self.var_actualizar_id.set(dato[3])
        self.var_actualizar_nombre.set(dato[0])
        self.var_actualizar_unidad.set(dato[1])
        self.var_actualizar_cu.set(dato[2])
    
    def actualizar_servicio(self):
        if self.var_actualizar_nombre.get()!="" and self.var_actualizar_unidad.get()!="":
            servicio=[
                self.var_actualizar_cu.get(),
                self.var_actualizar_unidad.get(),
                self.var_actualizar_nombre.get(),
                self.var_actualizar_id.get()]
            self.bbdd.actualizar_servicio(servicio)
            self.servicio_combobox["values"]=self.listar_servicios()
            self.servicio_combobox.current(0)
            self.var_actualizar_nombre.set("")
            self.var_actualizar_unidad.set("")
            self.var_actualizar_cu.set(0.0)
        else:
            messagebox.showinfo(message="Debe Seleccionar un Servicio",title="Error")

    def eliminar_servicio(self):
        if self.var_actualizar_nombre.get()!="" and self.var_actualizar_unidad.get()!="":
            if messagebox.askokcancel("Eliminar Servicio","Confirmar Eliminación"):
                self.bbdd.eliminar_servicio(self.var_actualizar_nombre.get())
                self.servicio_combobox["values"]=self.listar_servicios()
                self.servicio_combobox.current(0)
                self.var_actualizar_nombre.set("")
                self.var_actualizar_unidad.set("")
                self.var_actualizar_cu.set(0.0)
        else:
            messagebox.showinfo(message="Debe Seleccionar un Servicio",title="Error")