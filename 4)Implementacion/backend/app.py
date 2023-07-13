from main import create_app
from main import mongo
import time
import os
import  json
import requests
from oauthlib.oauth2 import WebApplicationClient
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
# from main.mail.funcion import sendMail

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

app = create_app()
app.app_context().push()


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
# import main.resources as resources
# threading.Thread(target=mandar_mail, args=(TIEMPO_MAIL,), name="Mandar email").start()

if __name__ == '__main__':
    app.run(debug = True, port = os.getenv('PORT'))