from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hola'
@app.route('/vias')
def vias():
    return 'Escriba el id de la via'
@app.route('/vias/1')
def via1():
    return 'Caricias de coral - 6b'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
