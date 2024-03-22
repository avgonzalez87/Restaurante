class UserManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def crear_usuario(self, nombre, apellido, correo, telefono, tipo_usuario, contrasena):
        conexion = self.db_connection.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                # Igual que en ReservaManager, simplificamos la consulta SQL eliminando sql.SQL
                query = """INSERT INTO usuarios(nombre, apellido, correo, telefono, tipo_usuario, contrasena) 
                           VALUES (%s, %s, %s, %s, %s, %s);"""
                cursor.execute(query, (nombre, apellido, correo, telefono, tipo_usuario, contrasena))
                conexion.commit()
                print("Usuario creado exitosamente.")
            except Exception as e:
                print(f"Ocurrió un error al crear el usuario: {e}")
                conexion.rollback()
            finally:
                cursor.close()
                self.db_connection.cerrar()