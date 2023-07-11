from flask import Flask, Response, jsonify, request
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_restful import Api
from dotenv import load_dotenv
api = Api()

mongo = PyMongo()

jwt = JWTManager()

def create_app():
    
    app = Flask(__name__)
    load_dotenv()

    app.secret_key = 'myawesomesecretkey'
    app.config['MONGO_URI'] = "mongodb+srv://microblog:microblog1234@cluster0.7houovt.mongodb.net/microblog?retryWrites=true&w=majority&ssl=true&tlsAllowInvalidCertificates=true"
    mongo.init_app(app)
    
    jwt.init_app(app)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

    import main.resources as resources

    api.add_resource(resources.UsuarioResource, '/usuario/<correo>')
    api.add_resource(resources.UsuariosResource, "/usuarios")

    api.init_app(app)

    jwt.init_app(app)

    from main.auth import routes
    app.register_blueprint(routes.auth)

    return app
