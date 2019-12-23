from tkinter import *
from tkinter import ttk
#importamos las vistas
from views.facturacion import *
from views.reportes import *
from views.proyectos import *
from views.servicios import *

class Vista_Index():
    def __init__(self,aplicacion):
        self.aplicacion=aplicacion
        self.menu=None
        #invocación de frames
        self.facturacion=Vista_Facturacion(self.aplicacion)
        self.reportes=Vista_Reportes(self.aplicacion)
        self.proyectos=Vista_Proyectos(self.aplicacion)
        self.servicios=Vista_Servicios(self.aplicacion)
        self.frames=[
            self.facturacion.frame_principal,
            self.reportes.frame_principal,
            self.proyectos.frame_principal,
            self.servicios.frame_principal
        ]

        self.nombres=["Facturación","Reportes", "Proyectos","Servicios"]
        #creamos el menu
        self.crearMenu()
        #llamamos a la facturación por defecto
        self.llamadaMenu(self.menu,2)
    
    def llamadaMenu(self,submenu,posicion):
        menu_elegido=submenu.entrycget(posicion,"label")
        for index,menu in enumerate(self.nombres):
            if menu==menu_elegido:
                self.frames[index].pack(fill=BOTH)
            else:
                self.frames[index].pack_forget()
    
    def crearMenu(self):
        #pegamos el menu a la ventana
        self.menu=Menu(self.aplicacion)
        #creamos los submenus
        administracion_subMenu=Menu(self.menu,tearoff=0)
        facturacion_subMenu=Menu(self.menu,tearoff=0)
        reportes_subMenu=Menu(self.menu,tearoff=0)
        #submenu especial del área de administracion
        administracion_subMenu.add_command(label="Proyectos", underline=0,command=lambda:self.llamadaMenu(administracion_subMenu,0))
        administracion_subMenu.add_command(label="Servicios", underline=0,command=lambda:self.llamadaMenu(administracion_subMenu,1))    
        

        #agregamos al menu principal
        self.menu.add_cascade(label="Administración",menu=administracion_subMenu)
        self.menu.add_command(label="Facturación", command=lambda: self.llamadaMenu(self.menu,2))
        self.menu.add_command(label="Reportes",command=lambda:self.llamadaMenu(self.menu,3))

