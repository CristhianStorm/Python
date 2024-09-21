#!/usr/bin/env python
# -*- Coding: utf-8 -*-

from flask import Flask, Blueprint, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import mysql.connector
from datetime import datetime
from time import sleep

app = Flask(__name__)
setrest01 = Blueprint('setrest01', __name__)

# Configuración de la base de datos
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1245678',
    'database': 'Examen'
}

# Ruta para el servicio de autenticación
@app.route('/setrest01', methods=['POST'])
def llamarServicioSet():
    data = request.json
    codigo = data['codigo']
    password = data['password']
    
    # Ejecutar la lógica de Selenium
    salida = inicializarVariables(codigo, password)
    
    return jsonify({'ParmOut': salida})

# Función principal para inicializar el driver de Selenium
def inicializarVariables(codigo, password):
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    # Configuración de Selenium
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chromedriver_path = 'C:\\Users\\Crisman\Documents\\Python\\Prueba\\chromedriver.exe'
    
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(15)
    
    try:
        driver.get('https://jaguarete.unida.edu.py/jaguarete/Login')
        accesoSet(driver, codigo, password)
    except TimeoutException:
        driver.close()
        driver.quit()
        print("No se pudo abrir la página Jaguarete!!!")
        return {"status": "error", "message": "Timeout en la página"}
    finally:
        driver.quit()
    
    return {"status": "success", "message": "Autenticación completa"}

# Función para automatizar el acceso con Selenium
def accesoSet(driver, codigo, password):
    url_jaguarete = 'https://jaguarete.unida.edu.py/jaguarete/Login'
    
    try:
        codigo_input = driver.find_element(By.ID, 'codigo')
        codigo_input.send_keys(codigo)
        sleep(5)
        
        password_input = driver.find_element(By.ID, 'password')
        password_input.send_keys(password)
        sleep(5)
        
        login_button = driver.find_element(By.XPATH, '//*[text()="Ingresar"]')
        login_button.click()
        sleep(5)
        
        # Registrar el evento de autenticación en la base de datos
        registrar_evento(codigo, url_jaguarete)
        
    except Exception as e:
        print("ERROR EN: login, intentando cerrar el driver", str(e))

# Función para registrar el evento en la base de datos MySQL
def registrar_evento(matricula, url_visita):
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor()
        
        query = """INSERT INTO registros_autenticacion (matricula, url_visita, fecha_hora)
                   VALUES (%s, %s, %s)"""
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(query, (matricula, url_visita, fecha_hora_actual))
        
        conexion.commit()
    
    except mysql.connector.Error as err:
        print(f"Error al registrar en la base de datos: {err}")
    
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

if __name__ == '__main__':
    app.register_blueprint(setrest01)
    app.run(host='0.0.0.0', port=5000, debug=True)
