from datetime import date
#importamos controlador de bbdd
from controllers.datos import *

class Controlador_Auxiliares():

    def __init__(self):
        self.bbdd=Controlador_BBDD()

    def obtenerFecha(self):
        fecha=date.today()
        dia=fecha.strftime("%d/%m/%Y")
        return dia
    
    def crearCodigo(self,proyecto):
        prefijo="SL-"
        #obtenemos el año
        ano=self.obtener_ano()
        subsidio=self.cs_ss(proyecto)
        numero=self.obtener_codigos_registro(proyecto)
        codigo=prefijo+ano+subsidio+str(numero)
        return codigo
    
    def cs_ss(self,proyecto):
        #micro función que determina si es subsidio o no
        if proyecto!="Ninguno":
            return "-CS-"
        else:
            return "-SS-"
    
    def obtener_ano(self):
        dia=self.obtenerFecha()
        aux=dia.split("/")
        ano=aux[2]
        return ano
    
    def obtener_codigos_registro(self,proyecto):
        resultados=self.bbdd.obtener_codigos_registro(proyecto)
        codigos=[]
        for resultado in resultados:
            codigos.append(self.desglose(resultado[0]))
        numero=max(codigos)+1
        return numero
        #print(max(codigos))
    
    def desglose(self,resultado):
        codigo=resultado.split("-")
        numero=codigo[3]
        return int(numero)