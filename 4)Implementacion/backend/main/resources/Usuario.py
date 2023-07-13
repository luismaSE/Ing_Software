from flask_restful import Resource
from flask import request, jsonify, session, Response
from .. import mongo
from bson import json_util
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from main.auth.decorators import admin_required
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import Usuario
from main.mail.funcion import sendMail

class Usuario(Resource):

    #! Perfil de usuario

    def get(self, alias):
        user = mongo.db.users.find_one({'alias': alias})
        response = json_util.dumps(user)
        return Response(response, mimetype="application/json")

    #! Seguir o dejar de seguir
    @jwt_required()
    def put(self, alias):
        
        
        seguido = mongo.db.users.find_one({"alias": alias})
        if seguido is None:
            return "Usuario inexistente", 409

        claims = get_jwt()
        mi_alias = claims["alias"]
        mi_usuario = mongo.db.users.find_one({"alias": mi_alias}) 
        
        if mi_alias == alias:
            return "No te podes autoseguir.", 409

        if mi_alias in seguido["seguidores"]:
            mongo.db.users.update_one({"alias": alias},{'$pull': {'seguidores': mi_alias}})
            mongo.db.users.update_one({"alias": mi_alias},{'$pull': {'seguidos': alias}})
            return "Dejaste seguir a '{}'".format(alias), 200

        mongo.db.users.update_one({"alias": alias},{'$push': {'seguidores': mi_alias}})
        mongo.db.users.update_one({"alias": mi_alias}, {'$push': {'seguidos': alias}})

        return "Comenzaste de seguir a '{}'".format(alias), 200

    # @app.route('/users/<id>', methods=['DELETE'])
    # def delete_user(id):
    #     mongo.db.users.delete_one({'_id': ObjectId(id)})
    #     response = jsonify({'message': 'User' + id + ' Deleted Successfully'})
    #     response.status_code = 200
    #     return response


    # @app.route('/users/<_id>', methods=['PUT'])
    # def update_user(_id):
    #     username = request.json['username']
    #     email = request.json['email']
    #     password = request.json['password']
    #     if username and email and password and _id:
    #         hashed_password = generate_password_hash(password)
    #         mongo.db.users.update_one(
    #             {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'username': username, 'email': email, 'password': hashed_password}})
    #         response = jsonify({'message': 'User' + _id + 'Updated Successfuly'})
    #         response.status_code = 200
    #         return response
    #     else:
    #         return not_found()
        
class Usuarios(Resource):

    #! Obtener todos los usuarios

    def get(self):
        users = mongo.db.users.find()
        response = json_util.dumps(users)
        return Response(response, mimetype="application/json")


class UsuariosEncontrados(Resource):

    #! Lista de usuarios

    def get(self, alias):
        user = mongo.db.users.find({'alias': {'$regex': alias, '$options': 'i'}})
        response = json_util.dumps(user)
        return Response(response, mimetype="application/json")


class Admin(Resource):

    @admin_required
    def get(self,dias):

        sendMail("tinchoreyes123@gmail.com", "Temas")

