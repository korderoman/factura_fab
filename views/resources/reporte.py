from fpdf import FPDF

class Reporte():
    def __init__(self):
        self.pdf=FPDF('L') #creamos una instancia
    
    def crear_reporte(self,servicio,proyecto,desde,hasta,reporte,total):
        self.pdf.add_page()
        self.pdf.image("./images/cabecera.png",x=10,y=8,w=190)
        self.pdf.image("./images/informacion_contacto.png",x=10,y=45,w=190)
        self.pdf.set_font("Arial",size=12)
        ancho_columna=self.pdf.w/5.5 #definimos el ancho de la columna
        alto_fila=self.pdf.font_size+1 #definimos el alto de la fila

        self.pdf.ln(65)
        self.pdf.cell(0,alto_fila,txt="Servicio: "+servicio)
        self.pdf.ln(alto_fila)
        self.pdf.cell(0,alto_fila,txt="Proyecto: "+proyecto)
        self.pdf.ln(alto_fila)
        self.pdf.cell(0,alto_fila,txt="Desde: "+desde +" Hasta: "+hasta)
        self.pdf.ln(alto_fila)
        self.pdf.cell(0,alto_fila,txt="Costo Total: "+str(total))
        self.pdf.ln(alto_fila)

        #print(reporte)

        elementos=["Código","Solicitante","N° Identidad","Detalle","Tiempo","Costo Total"]
        self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(elementos[0]),border=1)
        self.pdf.cell(ancho_columna*1.5,alto_fila,txt=str(elementos[1]),border=1)
        self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(elementos[2]),border=1)
        self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(elementos[3]),border=1)
        self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(elementos[4]),border=1)
        self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(elementos[5]),border=1)
        self.pdf.ln(alto_fila)
        for fila in reporte:
                self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(fila[1]),border=1)
                self.pdf.cell(ancho_columna*1.5,alto_fila,txt=str(fila[2]),border=1)
                self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(fila[4]),border=1)
                self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(fila[5]),border=1)
                self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(fila[8]),border=1)
                self.pdf.cell(ancho_columna/1.5,alto_fila,txt=str(fila[11]),border=1)
                self.pdf.ln(alto_fila)
        self.pdf.output("reportes.pdf")