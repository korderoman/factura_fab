import sqlite3

class Controlador_BBDD():
    def __init__(self):
        pass

    def consultar(self,consulta,variables=None):
        try:
            conexion=sqlite3.connect("./controllers/bbdd.db")
            cursor=conexion.cursor()
            if variables:
                #recuerda que la consulta debe llegar en formato de lista
                cursor.execute(consulta,variables)
            else:
                cursor.execute(consulta)
            
            resultados=cursor.fetchall()
            conexion.commit()
            conexion.close()
            return resultados
        except sqlite3.Error as error:
            print(error)
        
        


    #proyectos
    def obtener_proyectos(self):
        consulta="select nombre from proyectos"
        resultados=self.consultar(consulta)
        return resultados
    
    def obtener_proyecto(self,proyecto):
        consulta="select * from proyectos where nombre=?"
        variables=[]
        variables.append(proyecto)
        resultados=self.consultar(consulta,variables)
        #print(resultados)
        return resultados[0]

    def agregar_proyecto(self,proyecto):
        consulta="insert into proyectos values (?,?,?,?,NULL)"
        self.consultar(consulta,proyecto)

    def actualizar_proyecto(self,proyecto):
        consulta="update proyectos set universidad=?, facultad=?, responsable=? , nombre=? where id=?"
        self.consultar(consulta,proyecto)

    #servicios
    def obtener_servicios(self):
        consulta="select nombre from servicios"
        resultados=self.consultar(consulta)
        #print(resultados)
        return resultados
    
    def obtener_servicio(self,servicio):
        consulta="select * from servicios where nombre=?"
        variables=[]
        variables.append(servicio)
        resultados=self.consultar(consulta,variables)
        return resultados[0] #devuelve una tupla
    
    def actualizar_servicio(self,servicio):
        consulta="update servicios set cu=?, unidad=?, nombre=? where id=?"
        self.consultar(consulta,servicio)
    
    def eliminar_servicio(self,nombre):
        consulta="delete from servicios where nombre=?"
        self.consultar(consulta,[nombre])

    def agregar_servicio(self,servicio):
        consulta="insert into servicios values (?,?,?,NULL)"
        self.consultar(consulta,servicio)

    #registros de facturación
    def obtener_codigos_registro(self,proyecto):
        if proyecto=="Ninguno":
            consulta="select CODIGO from registros where PROYECTO='Ninguno'"
        else:
            consulta="select CODIGO from registros where not PROYECTO='Ninguno'"
        resultados=self.consultar(consulta)
        return resultados
    
    def agregar_registro(self,registro):
        consulta="insert into registros values (NULL,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.consultar(consulta,registro)