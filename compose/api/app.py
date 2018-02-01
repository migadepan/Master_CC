from flask import Flask
from flask import request
from model import db
from model import Via
from model import CreateDB
from model import app as application
import simplejson as json
from sqlalchemy.exc import IntegrityError
import os

# initate flask app
app = Flask(__name__)

@app.route('/')
def index():
	return 'API en Flask y Mysql para el almacenamiento de vias de escalada'

@app.route('/via')
def show_via():
	try:
		via = Via.query.filter_by(name=request.args['name']).first_or_404()
		return json.dumps({via.name:{ 'grade': via.grade, 'place': via.place,'style':via.style}})
	except IntegrityError:
		return json.dumps({})

@app.route('/insert')
def insert_via():
	try:
		via = Via(request.args['name'], 
				request.args['grade'], 
				request.args['place'], 
				request.args['style'])
		db.session.add(via)
		db.session.commit()
		return json.dumps({'status':True})
	except IntegrityError:
		return json.dumps({'status':False})

@app.route('/insertAll')
def insert_via_all():
	try:
		via = Via('Caricias de coral','6b','Alfacar','Deportiva')
		via2 = Via('Frio polar','6a+','Alfacar','Deportiva')
		via3 = Via('Bloquea o muere','6b','Alfacar','Deportiva')
		via4 = Via('Mahoma o filemon','7a','Alfacar','Deportiva')
		db.session.add(via)
		db.session.add(via2)
		db.session.add(via3)
		db.session.add(via4)
		db.session.commit()
		return json.dumps({'status':True})
	except IntegrityError:
		return json.dumps({'status':False})

@app.route('/vias')
def vias():
	try:
		vias = Via.query.all()
		vias_dict = {}
		for via in vias:
			vias_dict[via.name] = {
							'grade': via.grade,
							'place': via.place,
							'style': via.style
						    }

		return json.dumps(vias_dict)
	except IntegrityError:
		return json.dumps({})

@app.route('/createdb')
def createDatabase():
	try:
		HOSTNAME = 'myapirest'
		database = CreateDB(hostname = HOSTNAME)
		db.create_all()
		return json.dumps({'status':True})
	except IntegrityError:
		return json.dumps({'status':False})

@app.route('/status')
def app_status():
	return json.dumps({'status':True}), 200, {'ContentType':'application/json'}

@app.route('/info')
def app_info():
	return json.dumps({'server_info':application.config['SQLALCHEMY_DATABASE_URI']})

# run app service 
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)

