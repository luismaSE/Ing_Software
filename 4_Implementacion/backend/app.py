from main import create_app
from flask import Flask
from flask_pymongo import PyMongo
import os

from dotenv import load_dotenv
from flask_restful import Api
from flask_jwt_extended import JWTManager

app = create_app()

app.app_context().push()

app.config["MONGO_URI"] = os.getenv('DATABASE_CLIENT')
mongo = PyMongo(app)


if __name__ == '__main__':
	# db.create_all()
	app.run(debug = True, port = os.getenv("PORT"))