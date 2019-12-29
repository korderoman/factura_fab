from tkinter import *
from tkinter import ttk
from controllers.datos import *
from controllers.auxiliares import *
#calendario
from tkcalendar import Calendar, DateEntry
#reporte
from views.resources.reporte import *

class Vista_Reportes():
    def __init__(self,aplicacion):
        #creamos una instancia de la bbdd
        self.bbdd=Controlador_BBDD()
        #creamos una instancia de las funciones auxiliares
        self.auxiliar=Controlador_Auxiliares()
        #creamos una instancia de reporte
        self.reportes=Reporte()
        self.mx=5
        self.my=5
        self.ancho=30
        
        #variables de formulario
        self.proyectos_combobox=None
        self.servicios_combobox=None
        self.calendario_desde=StringVar()
        self.calendario_hasta=StringVar()
        self.etiqueta_servicio=StringVar()
        self.etiqueta_proyecto=StringVar()
        self.etiqueta_desde=StringVar()
        self.etiqueta_hasta=StringVar()
        self.etiqueta_total=StringVar()


        self.aplicacion=aplicacion
        self.frame_principal=Frame(self.aplicacion)
        self.intefaz(self.frame_principal)

    def intefaz(self,padre):
        frame_reportes_variables=LabelFrame(padre,text="Variables de Reporte")
        frame_reportes_preliminar=LabelFrame(padre,text="Vista Preliminar")

        #contenido del frame variables
        Label(frame_reportes_variables,text="Buscar por nombre del Servicio: ").grid(row=0, column=0,padx=self.mx,pady=self.my,sticky=W)
        self.servicios_combobox=ttk.Combobox(frame_reportes_variables,state="readonly",width=self.ancho-3)
        self.servicios_combobox["values"]=["Todos","Corte Láser","Escaneado 3D","Ruteadora CNC","Impresión 3D"]
        self.servicios_combobox.current(0)
        self.servicios_combobox.grid(row=0,column=1, padx=self.mx,pady=self.my,sticky=W)

        Label(frame_reportes_variables,text="Buscar por nombre del Proyecto: ").grid(row=1, column=0,padx=self.mx,pady=self.my,sticky=W)
        self.proyectos_combobox=ttk.Combobox(frame_reportes_variables,state="readonly",width=2*self.ancho-20)
        self.proyectos_combobox["values"]=self.listar_proyectos()
        self.proyectos_combobox.current(0)
        self.proyectos_combobox.grid(row=1,column=1, padx=self.mx,pady=self.my,sticky=W)

        #almanaque
        Label(frame_reportes_variables,text="Desde:").grid(row=2, column=0,padx=self.mx,pady=self.my,sticky=W)
        DateEntry(frame_reportes_variables,width=12,textvariable=self.calendario_desde,background="darkblue",foreground="white",borderwidth=2,day=1,month=1,year=2019).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Label(frame_reportes_variables,text="Hasta:").grid(row=3, column=0,padx=self.mx,pady=self.my,sticky=W)
        DateEntry(frame_reportes_variables,width=12,textvariable=self.calendario_hasta,background="darkblue",foreground="white",borderwidth=2,year=2019).grid(row=3,column=1,padx=self.mx,pady=self.my,sticky=W+E)
        Button(frame_reportes_variables,text="Obtener Reporte", command=lambda:self.obtener_reporte(frame_reportes_preliminar)).grid(row=4,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        #contenido del frame preliminar




        frame_reportes_variables.pack(side="left", fill=Y)
        frame_reportes_preliminar.pack(side="left", fill=Y)
    """   
    def listar_servicios(self):
        servicios=["Todos"]
        resultados=self.bbdd.obtener_servicios()
        for resultado in resultados:
            servicios.append(resultado[0])
        return servicios
    """
    def obtener_reporte(self,frame):
        servicio=self.servicios_combobox.get()
        proyecto=self.proyectos_combobox.get()
        aux_desde=self.calendario_desde.get().split("/")
        aux_hasta=self.calendario_hasta.get().split("/")
        desde="20"+aux_desde[2]+"-"+aux_desde[1]+"-"+aux_desde[0]
        hasta="20"+aux_hasta[2]+"-"+aux_hasta[1]+"-"+aux_hasta[0]
        reporte=self.auxiliar.obtener_reporte(servicio,proyecto,desde,hasta)
        #print(reporte)
        total=self.auxiliar.obtener_totales(reporte)
        self.interfaz_frame_preliminar(frame,servicio,proyecto,desde,hasta,reporte,total)
         
        #print(total)

    def listar_proyectos(self):
        proyectos=["Todos"]
        resultados=self.bbdd.obtener_proyectos()
       
        for resultado in resultados:
            proyectos.append(resultado[0])
        return proyectos
    
    def interfaz_frame_preliminar(self,frame,servicio,proyecto,desde,hasta,reporte,total):
        self.etiqueta_servicio.set("Servicio: "+servicio)
        self.etiqueta_proyecto.set("Proyecto: "+proyecto)
        self.etiqueta_desde.set("Desde: "+ desde)
        self.etiqueta_hasta.set("Hasta: "+hasta)
        self.etiqueta_total.set("Costo Total: "+str(total))

        Label(frame,textvariable=self.etiqueta_servicio).grid(row=0,column=0,padx=self.mx,pady=self.my,sticky=W)
        Label(frame,textvariable=self.etiqueta_proyecto).grid(row=1,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W)
        Label(frame,textvariable=self.etiqueta_desde).grid(row=2,column=0,padx=self.mx,pady=self.my,sticky=W)
        Label(frame,textvariable=self.etiqueta_hasta).grid(row=2,column=1,padx=self.mx,pady=self.my,sticky=W)
        tabla=ttk.Treeview(frame,columns=("1"))
        
        tabla.column("#0",width=50)
        tabla.column("1",width=15)
        for dato in reporte:
            tabla.insert("","end",text=str(dato[1]),values=(str(dato[11])))
        tabla.grid(row=3,column=0,columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)
        tabla.heading("#0",text="Código",anchor="center")
        tabla.heading("1",text="Costo",anchor="center")
        Label(frame,textvariable=self.etiqueta_total).grid(row=4,column=1,columnspan=2,padx=self.mx,pady=self.my,sticky=W)
        Button(frame,text="Imprimir Reporte Detallado (PDF)", command=lambda:self.imprimir_pdf(servicio,proyecto,desde,hasta,reporte,total)).grid(row=5,column=0, columnspan=2,padx=self.mx,pady=self.my,sticky=W+E)

    def imprimir_pdf(self,servicio,proyecto,desde,hasta,reporte,total):
        self.reportes.crear_reporte(servicio,proyecto,desde,hasta,reporte,total)