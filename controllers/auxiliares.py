from datetime import date
#importamos controlador de bbdd
from controllers.datos import *

class Controlador_Auxiliares():

    def __init__(self):
        self.bbdd=Controlador_BBDD()

    def obtenerFecha(self):
        fecha=date.today()
        dia=fecha.strftime("%Y-%m-%d")
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
        aux=dia.split("-")
        ano=aux[0]
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

    def obtener_reporte(self,servicio,proyecto,desde,hasta):
        if servicio=="Todos" and  proyecto=="Todos":
            consulta="select * from registros where DATE(fecha) between '{0}' and '{1}'".format(desde,hasta)
            return self.bbdd.obtener_reporte(consulta)
        elif servicio!="Todos" and proyecto=="Todos":
            
            consulta="select * from registros where SERVICIO like '{0}%' and DATE(fecha) between  '{1}' and '{2}' ".format(servicio,desde,hasta)
            return self.bbdd.obtener_reporte(consulta)
        elif servicio=="Todos" and proyecto!="Todos":
            consulta="select * from registros where PROYECTO=? and DATE(fecha) between  '{0}' and '{1}'".format(desde,hasta)
            return self.bbdd.obtener_reporte(consulta,[proyecto])
        elif servicio!="Todos" and proyecto!="Todos":
            consulta="select * from registros where SERVICIO like '{0}%' and PROYECTO='{1}' and DATE(fecha) between  '{2}' and '{3}'".format(servicio,proyecto,desde,hasta)
            return self.bbdd.obtener_reporte(consulta)

    def obtener_totales(self,resultados):
        suma=0
        for resultado in resultados:
            suma+=float(resultado[11])
        return suma



