from main import create_app
from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
# from main import db
import os , certifi


app = create_app()
app.app_context().push()

# client  = MongoClient(os.getenv('DATABASE_CLIENT'),  tlsCAFile=certifi.where())
# app.config[]

app.config["MONGO_URI"] = os.getenv('DATABASE_CLIENT')
mongo = PyMongo(app)

if __name__ == '__main__':
	# db.create_all()
	app.run(debug = True, port = os.getenv("PORT"))