from flask_restful import Resource
from flask import request, jsonify, session, Response
from .. import mongo
from bson import json_util
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import re


class Mensajes(Resource):
    
    @jwt_required()
    def post(self):

        texto = request.json['texto']

        if len(texto) > 140:
            return "El texto no puede tener mas de 140 caracteres.", 409 

        hashtags = re.findall(r'#(\w+)', texto)
        menciones = re.findall(r'@(\w+)', texto)
        claims = get_jwt()
        autor = claims["alias"]
        fecha = datetime.now().strftime("%H:%M %d-%m-%Y")

        id = mongo.db.messages.insert_one(
                {
                'texto': texto,
                "hashtags": hashtags,
                "menciones": menciones, 
                'autor': autor,
                "fecha": fecha,
                }
            )
        response = jsonify(
                {
                '_id': str(id),
                'texto': texto,
                "hashtags": hashtags,
                "menciones": menciones, 
                'autor': autor,
                "fecha": fecha,
                }
            )
        response.status_code = 201
        
        return response


    @jwt_required()
    def get(self):

        claims = get_jwt()
        alias = claims["alias"]

        datos = mongo.db.users.find_one({"alias":alias})

        seguidos = datos["seguidos"]

        mensajes = mongo.db.messages.find({"autor": {"$in": seguidos}}).sort("fecha", -1)
 
        response = json_util.dumps(mensajes)
        
        return Response(response, mimetype="application/json")

        
class Mensaje(Resource):
    @jwt_required()
    def delete(self, _id):
        claims = get_jwt()
        autor = claims["alias"]

        from bson import ObjectId
        object_id = ObjectId(_id)
    
        autor_mensaje = mongo.db.messages.find_one({"_id":object_id, "autor":autor})
        
        if autor_mensaje is None:
            return "No podes borrar mensaje ajenos", 403

        mongo.db.messages.delete_one({'_id': object_id})

        return "Mensaje eliminado", 201


class MensajesAutor(Resource):
    # Para ver muro de usuario
    def get(self, autor):
        mensajes = mongo.db.messages.find_one({'autor': autor, })
        response = json_util.dumps(mensajes)
        if response == "null":
            return "No existe mensajes con el autor '{}'".format(autor), 404
        return Response(response, mimetype="application/json")
