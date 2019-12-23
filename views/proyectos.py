from tkinter import *
from tkinter import ttk
#importamos el controlador
from controllers.datos import *

class Vista_Proyectos():
    def __init__(self,aplicacion):
        #creamos una instancia de la bbdd
        self.bbdd=Controlador_BBDD()
        self.mx=5
        self.my=5
        self.ancho=30
        self.aplicacion=aplicacion
        #variables de formulario
        self.var_nuevo_nombre=StringVar()
        self.var_nuevo_universidad=StringVar()
        self.var_nuevo_facultad=StringVar()
        self.var_nuevo_responsable=StringVar()
        self.proyecto_combobox=None

        self.var_actualizar_id=IntVar()
        self.var_actualizar_nombre=StringVar()
        self.var_actualizar_universidad=StringVar()
        self.var_actualizar_facultad=StringVar()
        self.var_actualizar_responsable=StringVar()
        #frames
        self.frame_principal=Frame(self.aplicacion)
        #se implementa la interfaz
        self.interfaz(self.frame_principal)

    def interfaz(self,padre):
        frame_nuevo=LabelFrame(padre,text="Nuevo Proyecto")
        frame_actualizar=LabelFrame(padre,text="Actualizar Proyecto")
        #contenido del frame nuevo
        Label(frame_nuevo,text="Nombre del Proyecto: ").grid(row=0, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_nombre,width=self.ancho).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_nuevo,text="Universidad: ").grid(row=1, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_universidad,width=self.ancho).grid(row=1,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_nuevo,text="Facultad: ").grid(row=2, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_facultad,width=self.ancho).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(frame_nuevo,text="Responsable: ").grid(row=3, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_nuevo,textvariable=self.var_nuevo_responsable,width=self.ancho).grid(row=3,column=1,padx=self.mx,pady=self.my,sticky=W)
        Button(frame_nuevo,text="Agregar",command=lambda:self.agregar_proyecto()).grid(row=4,column=0,padx=self.mx,pady=self.my, sticky=W+E)
        #contenido del frame actualizar
        self.proyecto_combobox=ttk.Combobox(frame_actualizar, state="readonly",width=(2*self.ancho))
        self.proyecto_combobox["values"]=self.listar_proyectos()
        self.proyecto_combobox.current(0)
        self.proyecto_combobox.grid(row=0,column=0, columnspan=2, padx=self.mx,pady=self.my,sticky=W)
        Button(frame_actualizar,text="Buscar",command=lambda:self.obtener_proyecto(self.proyecto_combobox.get())).grid(row=0,column=2,padx=self.mx,pady=self.my,sticky=W+E)
        Label(frame_actualizar,text="Nombre del Proyecto: ").grid(row=1, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_nombre,width=self.ancho).grid(row=1,column=1,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        Label(frame_actualizar,text="Universidad: ").grid(row=2, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_universidad,width=self.ancho).grid(row=2,column=1,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        Label(frame_actualizar,text="Facultad: ").grid(row=3, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_facultad,width=self.ancho).grid(row=3,column=1,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        Label(frame_actualizar,text="Responsable: ").grid(row=4, column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(frame_actualizar,textvariable=self.var_actualizar_responsable,width=self.ancho).grid(row=4,column=1,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        Button(frame_actualizar,text="Actualizar",command=lambda:self.actualizar_proyecto()).grid(row=5,column=0,columnspan=3,padx=self.mx,pady=self.my,sticky=W+E)

        frame_nuevo.pack(side="left",fill=Y)
        frame_actualizar.pack(side="left",fill=Y)

    #funciones de procesamiento
    def agregar_proyecto(self):
        if self.var_nuevo_nombre.get()!="" and self.var_nuevo_universidad.get()!="" and self.var_nuevo_facultad.get()!="" and self.var_nuevo_responsable.get()!="":
            if messagebox.askokcancel("Agregar Proyecto","Confirmar Agregar"):
                proyecto=[self.var_nuevo_nombre.get(),self.var_nuevo_universidad.get(),self.var_nuevo_facultad.get(),self.var_nuevo_responsable.get()]
                self.var_nuevo_nombre.set("")
                self.var_nuevo_universidad.set("")
                self.var_nuevo_facultad.set("")
                self.var_nuevo_responsable.set("")
                self.bbdd.agregar_proyecto(proyecto)
                self.proyecto_combobox["values"]=self.listar_proyectos()
                self.proyecto_combobox.current(0)
        else:
            messagebox.showinfo(message="Debe llenar todos los campos",title="Error")

    def listar_proyectos(self):
        datos=self.bbdd.obtener_proyectos()
        resultados=[]
        for dato in datos:
            resultados.append(dato[0])
        return resultados
    
    def obtener_proyecto(self,proyecto):
        dato=self.bbdd.obtener_proyecto(proyecto)
        self.var_actualizar_nombre.set(dato[0])
        self.var_actualizar_universidad.set(dato[1])
        self.var_actualizar_facultad.set(dato[2])
        self.var_actualizar_responsable.set(dato[3])
        self.var_actualizar_id.set(dato[4])

    def actualizar_proyecto(self):
        if self.var_nuevo_nombre.get()!="" and self.var_nuevo_universidad.get()!="" and self.var_nuevo_facultad.get()!="" and self.var_nuevo_responsable.get()!="":
            proyecto=[
                self.var_actualizar_universidad.get(),
                self.var_actualizar_facultad.get(),
                self.var_actualizar_responsable.get(),
                self.var_actualizar_nombre.get(),
                self.var_actualizar_id.get()
                ]
            self.bbdd.actualizar_proyecto(proyecto)
            self.proyecto_combobox["values"]=self.listar_proyectos()
            self.proyecto_combobox.current(0)
            self.var_actualizar_nombre.set("")
            self.var_actualizar_universidad.set("")
            self.var_actualizar_facultad.set("")
            self.var_actualizar_responsable.set("")
        else:
            messagebox.showinfo(message="Debe seleccionar un proyecto",title="Error")
