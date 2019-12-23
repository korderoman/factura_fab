from datetime import date

class Controlador_Auxiliares():

    def __init__(self):
        pass

    def obtenerFecha(self):
        fecha=date.today()
        dia=fecha.strftime("%d/%m/%Y")
        return dia
    
    def crearCodigo(self):
        prefijo="SL-"
        #obtenemos el año
        dia=self.obtenerFecha()
        aux=dia.split("/")
        ano=aux[2]
        codigo=prefijo+ano
        return codigo

    
