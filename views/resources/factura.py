from fpdf import FPDF

class Factura():
    def __init__(self):
        self.pdf=FPDF() # creamos una instancia
    
    def crear_pdf(self,registro):
        self.pdf.add_page() #creamos una página
        self.pdf.image("./images/cabecera.png",x=10,y=8,w=190)#agregamos la imagen del logo
        self.pdf.image("./images/informacion_contacto.png",x=10,y=45,w=190) #agregamos la información de contacto
        #Inicio de la información Dinámica
        self.pdf.set_font("Arial",size=14)#definimos la fuente y el tamaño de la fuente
        ancho_columna=self.pdf.w/4.5 #definimos el ancho de la columna
        alto_fila=self.pdf.font_size #definimos el alto de la fila
    
        self.pdf.ln(65)
        self.pdf.cell(0,alto_fila,txt="Código: "+str(registro[0]))
        self.pdf.ln(alto_fila)
        self.pdf.cell(0,alto_fila,txt="Solicitante: "+str(registro[1]))
        self.pdf.ln(alto_fila)
        self.pdf.cell(0,alto_fila,txt=str(registro[2]+": "+str(registro[3])))
        self.pdf.ln(alto_fila)
        self.pdf.cell(0,alto_fila,txt="Fecha: "+str(registro[11]))
        self.pdf.ln(alto_fila)

        elementos=[
            ["Servicio","Tiempo","Unidad","Costo"],
            [registro[6],registro[7],registro[8],registro[10]]
        ]
       
       
        self.pdf.ln(3*alto_fila) #saltamos a la línea 100
        for fila in elementos:
            for elemento in fila:
                self.pdf.cell(ancho_columna,alto_fila,txt=str(elemento),border=1)
            self.pdf.ln(alto_fila)
            


        #Fin de la información Dinámica

        
        self.pdf.image("./images/observaciones.png",x=10,y=190,w=190)#agregamos la imgane de observaciones
        self.pdf.output("factura.pdf")#generamos el pdf