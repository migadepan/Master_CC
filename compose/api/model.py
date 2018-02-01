from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# Configuracion de la base de datos
app = Flask(__name__)
DATABASE = 'mydatabase'
PASSWORD = 'mypassword'
USER = 'root'
HOSTNAME = 'db'

# Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s'%(USER, PASSWORD, HOSTNAME, DATABASE)
db = SQLAlchemy(app)

# Database migration command line
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Via(db.Model):

	# Modelo de datos de la tabla Via
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=True)
	grade = db.Column(db.String(4), unique=False)
	place = db.Column(db.String(120), unique=False)
	style = db.Column(db.String(120), unique=False)

	def __init__(self, name, grade, place, style):
		# inicializa las columnas
		self.name = name
		self.grade = grade
		self.place = place
		self.style = style

	def __repr__(self):
		return '<Via %r>' % self.name

class CreateDB():
	def __init__(self, hostname=None):
		if hostname != None:	
			HOSTNAME = hostname
		import sqlalchemy
		engine = sqlalchemy.create_engine('mysql://%s:%s@%s'%(USER, PASSWORD, HOSTNAME))
		engine.execute("CREATE DATABASE IF NOT EXISTS %s "%(DATABASE)) # crear la base de datos

if __name__ == '__main__':
	manager.run()
