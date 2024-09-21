from flask import Blueprint, request, jsonify
import mysql.connector
from mysql.connector import Error

login = Blueprint('login', __name__)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'mysql-container',        # Cambia esto si tu base de datos está en un contenedor Docker
    'user': 'unida',     # Reemplaza con tu usuario de base de datos
    'password': 'unida123', # Reemplaza con tu contraseña de base de datos
    'database': 'jaguarete'  # Reemplaza con el nombre de tu base de datos
}

@login.route('/login', methods=['POST'])
def llamarServicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
    
    codRes, menRes, usuario, accion = verificar_credenciales(user, password)

    salida = {
        'codRes': codRes,
        'menRes': menRes,
        'usuario': usuario,
        'accion': accion
    }
    return jsonify(salida)

def verificar_credenciales(user, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    usuario = None
    
    try:
        print("Verificar login")
        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        
        # Ejecutar la consulta SQL
        query = "SELECT username FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (user, password))
        
        # Obtener el resultado
        result = cursor.fetchone()
        
        if result:
            usuario = result['username']
            print("Usuario y contraseña OK")
            accion = "Success"
        else:
            print("Usuario o contraseña incorrecta")
            accion = "Usuario o contraseña incorrecta"
            codRes = 'ERROR'
            menRes = 'Credenciales incorrectas'
        
        cursor.close()
        connection.close()
        
    except Error as e:
        print("ERROR", str(e))
        codRes = 'ERROR'
        menRes = 'Msg: ' + str(e)
        accion = "Error interno"

    return codRes, menRes, usuario, accion
