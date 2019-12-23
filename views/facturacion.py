from tkinter import *
from tkinter import ttk
#importamos los controladores
from controllers.datos import *
from controllers.auxiliares import *

class Vista_Facturacion():
    def __init__(self, aplicacion):
        #creamos una instancia de la bbdd
        self.bbdd=Controlador_BBDD()
        #creamos una instancia de los auxiliares
        self.auxiliar=Controlador_Auxiliares()
        #constantes de la aplicación
        self.mx=5
        self.my=5
        self.ancho=50
        self.aplicacion=aplicacion
        #variables del formulario
        self.var_solicitante=StringVar()
        self.var_tipoIdentidad=None #combobox
        self.var_servicio=None #combobox
        self.var_proyecto=None
        self.var_numeroIdentidad=StringVar()
        self.var_descripcion=StringVar()
        self.var_cantidad=DoubleVar()
        self.var_cu=DoubleVar()
        self.var_costo=DoubleVar()
        
        #implementación de la interfaz
        self.frame_principal=LabelFrame(self.aplicacion,text="Datos de Facturación")
        self.interfaz(self.frame_principal)

    def interfaz(self,padre):
        Label(padre,text="Solicitante: ").grid(row=0,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.var_solicitante,width=self.ancho).grid(row=0,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(padre,text="Tipo de Identidad: ").grid(row=1,column=0,padx=self.mx,pady=self.my,sticky=W)
        self.var_tipoIdentidad=ttk.Combobox(padre,state="readonly",width=self.ancho-3,values=["DNI","Extranjería","RUC"])
        self.var_tipoIdentidad.current(0)
        self.var_tipoIdentidad.grid(row=1,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(padre,text="Número de Identidad: ").grid(row=2,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.var_numeroIdentidad,width=self.ancho).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(padre,text="Descripción: ").grid(row=3,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.var_descripcion,width=self.ancho).grid(row=3,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(padre,text="Proyecto: ").grid(row=4,column=0,padx=self.mx,pady=self.my,sticky=W)
        self.var_proyecto=ttk.Combobox(padre,state="readonly",width=self.ancho-3)
        self.var_proyecto["values"]=self.listar_proyectos()
        self.var_proyecto.current(0)
        self.var_proyecto.grid(row=4,column=1,padx=self.mx,pady=self.my,sticky=W)
        Label(padre,text="Servicio: ").grid(row=5,column=0,padx=self.mx,pady=self.my,sticky=W)
        self.var_servicio=ttk.Combobox(padre,state="readonly",width=self.ancho-3)
        self.var_servicio["values"]=self.listar_servicios()
        self.var_servicio.bind("<<ComboboxSelected>>",self.costoUnitario)#evento a la escucha del cambio en el combobox
        self.var_servicio.current(0)
        self.var_servicio.grid(row=5,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(padre,text="Cantidad: ").grid(row=6,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.var_cantidad,width=self.ancho).grid(row=6,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(padre,text="Costo Unitario: ").grid(row=7,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.var_cu,width=self.ancho).grid(row=7,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Button(padre,text="Total", command=lambda:self.costoTotal()).grid(row=8,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        Label(padre,text="Costo Total: ").grid(row=9,column=0,padx=self.mx,pady=self.my,sticky=W)
        Entry(padre,textvariable=self.var_costo,width=self.ancho).grid(row=9,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Button(padre,text="Registrar", command=lambda:self.registrar()).grid(row=10,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
    
    #funciones auxiliares

    def costoUnitario(self,evento):
        servicio=self.bbdd.obtener_servicio(self.var_servicio.get())
        self.var_cu.set(servicio[2])

    def costoTotal(self):
        costo=self.var_cantidad.get()*self.var_cu.get()
        self.var_costo.set(costo)
        
    def listar_servicios(self):
        datos=self.bbdd.obtener_servicios()
        resultados=[]
        for dato in datos:
            resultados.append(dato[0])
        servicio=self.bbdd.obtener_servicio(resultados[0])
        self.var_cu.set(servicio[2])
        return resultados
    
    def listar_proyectos(self):
        resultados=["Ninguno"]
        datos=self.bbdd.obtener_proyectos()
        for dato in datos:
            resultados.append(dato[0])
        return resultados

    def registrar(self):
        fecha=self.auxiliar.obtenerFecha()
        codigo=self.auxiliar.crearCodigo()
        print(fecha,codigo)
        