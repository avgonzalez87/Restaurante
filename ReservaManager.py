class ReservaManager:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def crear_reserva(self, id_usuario, fecha, hora, numero_mesa, estado, detalle):
        conexion = self.db_connection.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
               
                query = """INSERT INTO reservas(id_usuario, fecha, hora, numero_mesa, estado, detalle) 
                           VALUES (%s, %s, %s, %s, %s, %s);"""  
                cursor.execute(query, (id_usuario, fecha, hora, numero_mesa, estado, detalle))
                conexion.commit()
                print("Reserva creada exitosamente.")
            except Exception as e:
                print(f"Ocurrió un error al crear la reserva: {e}")
                conexion.rollback()
            finally:
                cursor.close()
                self.db_connection.cerrar()