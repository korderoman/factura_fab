from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#importamos la vista index
from views.index import *
def salir():
    if messagebox.askokcancel("Salir de la Aplicación","¿Está seguro que desea salir?"):
        aplicacion.quit()
        aplicacion.destroy()


if __name__ == "__main__":
    aplicacion=Tk()
    # Inicio de Dimensión de la Aplicación
    ancho_programa=816
    alto_programa=490
    ancho_pantalla=aplicacion.winfo_screenwidth()
    alto_pantalla=aplicacion.winfo_screenheight()

    posicion_x=(ancho_pantalla/2)-(ancho_programa/2)
    posicion_y=(alto_pantalla/2)-(alto_programa/2)

    aplicacion.geometry("%dx%d+%d+%d"%(ancho_programa,alto_programa,posicion_x,posicion_y))
    aplicacion.resizable(False,False)
    #Fin de Dimensión de la Aplicación
    index=Vista_Index(aplicacion)
    aplicacion.config(menu=index.menu)

    aplicacion.title("Módulo de Facturación")
    aplicacion.protocol("WM_DELETE_WINDOW",salir)
    aplicacion.mainloop()



    



    