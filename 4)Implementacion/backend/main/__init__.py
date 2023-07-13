from flask import Flask, Response, jsonify, request, redirect, url_for , g
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_restful import Api
from dotenv import load_dotenv
from flask_mail import Mail
import os
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests, time
# from mail.funcion import sendMail


api = Api()

mongo = PyMongo()

jwt = JWTManager()

mailsender = Mail()

# TIEMPO_MAIL = os.environ.get("TIEMPO_MAIL")

# def mandar_mail(TIEMPO_MAIL):
#     # from bson import json_util
#     print("\n"*5, "Entrando en hilo emails...")
    
#     usuarios = mongo.db.users.find({}, {'correo': 1, 'alias': 1, 'nombre': 1})
#     # response = json_util.dumps(usuarios)
#     # print(Response(response, mimetype="application/json"))

#     tiempo = time.time()

#     time.sleep(10)

#     temas = resources.MensajesTendenciaResource.get()[0]

#     if tiempo > int(TIEMPO_MAIL):

# #-----------
#         for usuario in usuarios:
#             email = usuario['correo']
#             alias = usuario['alias']
#             nombre = usuario['nombre']
            
#             # Construir el contenido del correo con los datos del usuario
#             json_content = {
#                 'alias': alias,
#                 'nombre': nombre,
#                 'temas': temas
#             }
#             print("\n"*5, "Enviando emails...")
#             # Llamar a la función sendMail() para enviar el correo a cada usuario
#             sendMail(email, subject="Nuevos temas del momento", json_content=json_content)
# #-----------

# import threading
# import resources as resources
# threading.Thread(target=mandar_mail, args=(TIEMPO_MAIL,), name="Mandar email").start()


def create_app():
    
    app = Flask(__name__)
    load_dotenv()

    app.secret_key = os.getenv('SECRET_KEY')   #TODO << generar con  python -c 'import secrets; print(secrets.token_hex())' en la consola
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))                                                        #
    app.config['MONGO_URI'] = os.getenv('DATABASE_CLIENT')
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    mongo.init_app(app)
    jwt.init_app(app)
    
    # client = WebApplicationClient(GOOGLE_CLIENT_ID)

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
    api.add_resource(resources.DiasResource, "/dias")
    api.add_resource(resources.MensajesTendenciaResource, "/mensajestendencia")

    api.add_resource(resources.MensajePrivadoResource, "/mensajeprivado")   #Get, post

    app.config['MAIL_HOSTNAME'] = os.getenv('MAIL_HOSTNAME')
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS')
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['FLASKY_MAIL_SENDER'] = os.getenv('FLASKY_MAIL_SENDER')

    api.init_app(app)

    jwt.init_app(app)

    mailsender.init_app(app)

    from main.auth import routes
    app.register_blueprint(routes.auth)

    return app


#     @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)