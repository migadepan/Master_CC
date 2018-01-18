import requests
from flask import Flask
app = Flask(__name__)

@app.route('/vias')
def get_data():
    while True:
        requests.get('http://127.0.0.1:5000').content
        print('Peticion')
