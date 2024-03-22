import psycopg2
from psycopg2 import sql 

class DatabaseConnection:
    def __init__(self, host, database, user, password, port=5432):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.conexion = None  

    def conectar(self):
        try:
            self.conexion = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port)
            return self.conexion
        except Exception as e:
            print(f"Ocurrió un error al conectar a la base de datos: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()