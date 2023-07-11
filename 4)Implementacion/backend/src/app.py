from flask import Flask, jsonify, request, Response
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from flask_restful import Api
from bson import json_util
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, verify_jwt_in_request


app = Flask(__name__)

app.secret_key = 'myawesomesecretkey'

app.config['MONGO_URI'] = "mongodb+srv://microblog:microblog1234@cluster0.7houovt.mongodb.net/microblog?retryWrites=true&w=majority&ssl=true&tlsAllowInvalidCertificates=true"

mongo = PyMongo(app)

jwt = JWTManager(app)

app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

jwt.init_app(app)

# -------------------------------------------------------

@app.route('/register', methods=['POST'])
def register():
    #! campos obligatorios
    correo = request.json['correo']
    alias = request.json['alias']
    nombre = request.json['nombre']
    password = request.json['password']
    
    #! no obligatorio
    descripcion = request.json['descripcion']
    foto = request.json['foto']
    
    cuenta = mongo.db.users.find_one({"correo": correo})
    if cuenta == None:
        if correo and password:
            hashed_password = generate_password_hash(password)
            id = mongo.db.users.insert_one(
                {
                'correo': correo,
                "alias": alias,
                "nombre": nombre, 
                'password': hashed_password,
                "descripcion": descripcion,
                "foto": foto,
                "seguidores": [],
                "seguidos": [],
                "admin": 0
                }
            )
            response = jsonify(
                {
                '_id': str(id),
                'correo': correo,
                "alias": alias,
                "nombre": nombre, 
                'password': hashed_password,
                "descripcion": descripcion,
                "foto": foto,
                "seguidores": [],
                "seguidos": [],
                "admin": 0
                }
            )
            response.status_code = 201
            return response
        else:
            return not_found()
    else:
        return "Ya existe un usuario con ese email", 409


@app.route('/login', methods=['POST'])
def login():
    correo = request.json['correo']
    password = request.json['password']
    user = mongo.db.users.find_one({"correo": correo})
    password_hashed = user["password"]
    if check_password_hash(password_hashed, password):
        access_token = create_access_token(identity=correo)
        data = {
                'access_token': access_token
            }
        return data, 200
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response

# -------------------------------------------------------

@app.route('/users', methods=['GET'])
def get():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")


@app.route('/user/<correo>', methods=['GET'])
def get_user(correo):
    user = mongo.db.users.find_one({'correo': correo, })
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


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

# -------------------------------------------------------


if __name__ == "__main__":
    app.run(debug=True, port=3000)
