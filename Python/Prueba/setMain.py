###pip install --upgrade numpy pandas

from flask import Flask, jsonify, request
from setrest01 import setrest01

app = Flask(__name__) 

##servicios rest
app.register_blueprint(setrest01)

@app.route('/', methods=['GET'])
def hello():
    return 'Hola mundo'


if __name__ == "__main__":
    ## Solo necesitas una llamada a app.run()
    app.run(host='0.0.0.0', debug=True, port=5000)
