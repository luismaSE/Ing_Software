from flask_restful import Resource
from flask import request, Response
from .. import mongo
from bson import json_util
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime

class MensajesPrivado(Resource):

    #! Enviar mensaje privado    
    @jwt_required()
    def post(self):
        claims = get_jwt()
        emisor = claims["alias"]
        texto = request.json['texto']
        destinatario = request.json['destinatario']
        fecha = datetime.now().strftime("%H:%M %d-%m-%Y")
        
        if mongo.db.users.find_one({"alias":destinatario}) is None:
            return "Destinatario no existente.", 404
        
        if destinatario == emisor:
            return "No te podes autoenviar mensajes.", 409
            
        mongo.db.privatemessage.insert_one(
            {
                "emisor": emisor,
                "destinatario": destinatario,
                "texto": texto,
                "fecha": fecha,
            }
        )
        
        return "Mensaje enviado de {} a {}.".format(emisor, destinatario), 201

    #! Ver mensajes privados
    #TODO ordenar mensajes y agruparlos por pares de personas
    @jwt_required()
    def get(self):
        
        claims = get_jwt()
        alias = claims["alias"]

        mensajes_recibidos = mongo.db.privatemessage.find({"destinatario": alias}).sort([("emisor", 1), ("fecha", -1)])    
        mensajes_enviados = mongo.db.privatemessage.find({"emisor": alias}).sort([("emisor", 1), ("fecha", -1)])
        
        response = json_util.dumps({"enviados": mensajes_enviados, "recibidos": mensajes_recibidos})
        return Response(response, mimetype="application/json"), 200