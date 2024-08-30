from conexion_db import *
from datetime import date

class Tareas:
    fecha_actual = date.today()
    
    #MOSTRAR TAREAS
    def mostrar_tareas():
        try:
            conector = Conexion.conectar()
            cursor = conector.cursor()
            cursor.execute("SELECT * FROM tareas;")
            resultado = cursor.fetchall()
            conector.commit()
            conector.close()
            return resultado
        
        except mysql.connector.Error as error:
            print(f"Error al mostrar tareas {error}")
    
    #GUARDAR TAREA
    def guardar_tarea(usuario,nombre_tarea,descripcion):
        try:
            fecha_actual = date.today()
            conector = Conexion.conectar()
            cursor = conector.cursor()
            sql = "INSERT INTO tareas VALUES (null,%s,%s,%s,%s)"
            valores=(usuario,nombre_tarea,descripcion,fecha_actual)
            cursor.execute(sql,valores)
            conector.commit()
            print("Tarea guardada")
            conector.close()    
        except mysql.connector.Error as error:
            print(f"Error al guardar tarea {error}")
    #OBTENER TAREA COMPLETA (para almacenarla y luego usarla)
    @staticmethod
    def obtener_tarea_completa(idtarea):
        try:
            conector = Conexion.conectar()
            cursor = conector.cursor()
            sql = "SELECT tarea FROM tareas WHERE idtarea = %s;"
            valores = (idtarea,)
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()
            conector.close()
            if resultado:
                return resultado[0]
            else:
                return ""
        except mysql.connector.Error as error:
            return f"Error al obtener tarea completa: {error}"
    
    #MODIFICAR TAREA
    def modificar_tareas(nombre,nombre_tarea,tarea,idusuario):
        global fecha_actual
        try:
            fecha_actual = date.today()
            conector = Conexion.conectar()
            cursor = conector.cursor()
            sql=("UPDATE `tareas` SET `usuario` = %s, `nombre_tarea` = %s, `tarea` = %s, `fecha` = %s WHERE `tareas`.`idtarea` = %s;")
            valores = (nombre,nombre_tarea,tarea,fecha_actual,idusuario)
            cursor.execute(sql,valores)     
            conector.commit()
            print("Tarea modificada")
            conector.close()     
        except mysql.connector.Error as error:
            return f"Error al guardar tarea {error}"
    #Eliminar tarea
    def eliminar_tareas(idusuario):
        try:
            conector = Conexion.conectar()
            cursor = conector.cursor()
            sql=("DELETE FROM tareas WHERE `tareas`.`idtarea` = %s;")
            valores = (idusuario,)
            cursor.execute(sql,valores)     
            conector.commit()
            print("Tarea eliminada")
            conector.close()    
        except mysql.connector.Error as error:
            return f"Error al eliminar tarea {error}" 
            
