from flask import request, jsonify, Blueprint
from .. import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token


auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
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


@auth.route('/login', methods=['POST'])
def login():
    correo = request.json['correo']
    password = request.json['password']
    user = mongo.db.users.find_one({"correo": correo})
    password_hashed = user["password"]
    if check_password_hash(password_hashed, password):
        additional_claims = {"admin":user["admin"], "correo": user["correo"], "nombre": user["nombre"]}
        access_token = create_access_token(identity=correo,additional_claims=additional_claims)
        return jsonify(access_token=access_token),201
    else:
        return not_found()
    

@auth.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response
