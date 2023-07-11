from flask import request, jsonify, Blueprint
from flask_pymongo import PyMongo
from .. import __init__
# from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

# client = __init__.client
# client = app.db
auth = Blueprint('auth', __name__, url_prefix='/auth')

# @auth.route('/login', methods=['POST'])
# def login():
#     db = client['mydatabase']
#     collection = db['Usuarios']
#     correo = request.get_json().get("correo")
#     usuario = collection.find_one({"correo": correo})
#     print("\n"*5)
#     print(usuario)




@auth.route('/register', methods=['POST'])
def register():
    
    usuario = request.get_json()
    # db = client[]
    # data =  db.Usuarios.find_one()

    return usuario, 201

    # db = client


    # exists = db.session.query(UsuarioModel).filter(UsuarioModel.correo == usuario.correo).scalar() is not None

    # if exists:
    #     return 'Duplicated mail', 409
    # else:
    #     try:
    #         db.session.add(usuario)
    #         db.session.commit()
    #     except Exception as error:
    #         db.session.rollback()
    #         return str(error), 409
    #     return usuario.to_json() , 201