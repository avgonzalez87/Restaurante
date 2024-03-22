from flask import Flask, request, jsonify
from DatabaseConnection import DatabaseConnection
from UserManager import UserManager
from ReservaManager import ReservaManager

app = Flask(__name__)

# Configura aquí los detalles de tu base de datos
DB_HOST = "localhost"
DB_NAME = "Restaurante"
DB_USER = "postgres"
DB_PASSWORD = "adm"
DB_PORT = "5432"

db_connection = DatabaseConnection(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD, DB_PORT)
user_manager = UserManager(db_connection)
reserva_manager = ReservaManager(db_connection)

@app.route('/')
def home():
    return 'Bienvenido a la API de ReservaFacil!'

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario_endpoint():
    data = request.json
    try:
        user_manager.crear_usuario(data['nombre'], data['apellido'], data['correo'], data['telefono'], data['tipo_usuario'], data['contrasena'])
        return jsonify({"mensaje": "Usuario creado exitosamente."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/crear_reserva', methods=['POST'])
def crear_reserva_endpoint():
    data = request.json
    try:
        reserva_manager.crear_reserva(data['id_usuario'], data['fecha'], data['hora'], data['numero_mesa'], data['estado'], data['detalle'])
        return jsonify({"mensaje": "Reserva creada exitosamente."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '_main_':
    app.run(debug=True)