from flask import Flask, Response, jsonify, request
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_restful import Api
from dotenv import load_dotenv

api = Api()

login_manager = LoginManager()

mongo = PyMongo()

jwt = JWTManager()



def create_app():
    
    app = Flask(__name__)
    load_dotenv()

    app.secret_key = 'myawesomesecretkey'   # <<<<<<<<< generar con  python -c 'import secrets; print(secrets.token_hex())' en la consola
    app.config['MONGO_URI'] = "mongodb+srv://microblog:microblog1234@cluster0.7houovt.mongodb.net/microblog?retryWrites=true&w=majority&ssl=true&tlsAllowInvalidCertificates=true"
    
    login_manager.init_app(app)
    mongo.init_app(app)
    
    jwt.init_app(app)
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

    #! Para que siempre exista un admin
    admin = mongo.db.users.find_one({"admin": 1})    
    if admin == None:
        from werkzeug.security import generate_password_hash
        mongo.db.users.insert_one(
            {
            'correo': "admin@gmail.com",
            "alias": "admin",
            "nombre": "El Admin", 
            'password': generate_password_hash("123"),
            "descripcion": "Soy el Admin",
            "foto": "",
            "seguidores": [],
            "seguidos": [],
            "admin": 1
            }
        )


    import main.resources as resources

    api.add_resource(resources.UsuarioResource, '/usuario/<alias>')     #Get, put
    api.add_resource(resources.UsuariosResource, "/usuarios")   #Get
    api.add_resource(resources.UsuariosEncontradosResource, "/usuariosencontrados/<alias>")     #Get
    
    
    api.add_resource(resources.MensajesResource, "/mensajes")    #Post
    api.add_resource(resources.MensajeResource, "/mensaje/<_id>")    #Delete
    api.add_resource(resources.MensajesAutorResource, "/mensajes/<autor>")  #Get
    


    api.init_app(app)

    jwt.init_app(app)

    from main.auth import routes
    app.register_blueprint(routes.auth)

    return app
