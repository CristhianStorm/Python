#!/usr/bin/env python3
from flask import Flask
from urllib.parse import quote as url_quote
from flask_swagger_ui import get_swaggerui_blueprint
from login import login

app = Flask(__name__)

# Registrar el blueprint de login
app.register_blueprint(login)

# Definir la ruta de Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Ruta a tu archivo Swagger

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Login API"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola Mundo 2'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
