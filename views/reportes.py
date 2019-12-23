from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as tkst


class Vista_Reportes():
    def __init__(self,aplicacion):
        self.mx=5
        self.my=5
        self.aplicacion=aplicacion
        self.frame_principal=Frame(self.aplicacion)
        self.intefaz(self.frame_principal)

    def intefaz(self,padre):
        Label(padre,text="Reportes",justify=LEFT).grid(row=0,column=0,padx=self.mx,pady=self.my,sticky=W)