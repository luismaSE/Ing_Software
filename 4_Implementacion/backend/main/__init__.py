import os
from flask import Flask
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from flask_restful import Api
from flask_jwt_extended import JWTManager
import certifi

# from main.auth import routes


api = Api()
jwt = JWTManager()
load_dotenv()
client  = MongoClient(os.getenv('DATABASE_CLIENT'),  tlsCAFile=certifi.where())


def create_app():
	app = Flask(__name__)
	load_dotenv()
	
 	#TODO agregar admin
	# dbs = client.list_database_names()
	# if "microblog" not in dbs:
	# 	db=client[str(os.getenv('DATABASE_NAME'))]
	# 	# Crear una colección
	# 	coleccion = db["Usuarios"]
	# 	# Crear un documento
	# 	documento = {"nombre": "Ejemplo", "edad": 25}

	# 	coleccion.insert_one(documento)




	# import main.resources as resources
	# api.add_resource(resources.PoemaResource, '/poema/<poema_id>')
	
	api.init_app(app)
	
	app.config['PROPAGATE_EXCEPTIONS'] = True
	app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
	app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
	jwt.init_app(app)

	from main.auth import routes
	app.register_blueprint(auth.routes.auth)

	return app