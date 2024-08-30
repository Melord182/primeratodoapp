# pip install mysql-connector.python
import mysql.connector 


class Conexion:
    def conectar():
        config = {
            "user":'root',
            "password":'',
            "host":'localhost',
            "database": 'todoapp',
        }
        try:
            conn = mysql.connector.connect(**config)
            print("Conexion exitosa")
            return conn
        except mysql.connector.Error as error:
            print(f"Error en la conexion {error}")
            return None
