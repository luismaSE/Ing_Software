import os
from flask import Flask
from dotenv import load_dotenv
import pymongo
from pymongo import MongoClient
from flask_restful import Api
from flask_jwt_extended import JWTManager

api = Api()

jwt = JWTManager()


def jls_extract_def():
    #EJEMPLO
    return 


def create_app():
	app = Flask(__name__)
	load_dotenv()

	print("iniciando db")
	client = MongoClient('mongodb+srv://microblog:microblog1234@cluster0.7houovt.mongodb.net/?retryWrites=true&w=majority')
	print(client.server_info())
	dbs = client.list_database_names()
	print("sin", dbs)


	# import main.resources as resources
	# api.add_resource(resources.PoemaResource, '/poema/<poema_id>')                                                   #EJEMPLO = jls_extract_def()
	
	api.init_app(app)
	
	# app.config['PROPAGATE_EXCEPTIONS'] = True
	# app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
	# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
	# jwt.init_app(app)

	# from main.auth import routes
	# app.register_blueprint(auth.routes.auth)                                                                         #No se si va
    
	return app
