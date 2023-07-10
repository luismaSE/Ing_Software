from flask import request, jsonify, Blueprint
# from .. import db
# from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

auth = Blueprint('auth', __name__, url_prefix='/auth')

# @auth.route('/login', methods=['POST'])
# def login():
#     usuario = db.session.query(UsuarioModel).filter(UsuarioModel.correo == request.get_json().get("correo")).first_or_404()
#     if usuario.validacion_contra(request.get_json().get("contra")):
#         if not usuario.pendiente:
#             access_token = create_access_token(identity=usuario)
#             data = {
#                 'access_token': access_token
#             }
#             return data, 200
#         else:
#             return 'Usuario Pendiente de Aceptación', 401

#     else:
#         return 'Incorrect password', 401


# @auth.route('/register', methods=['POST'])
# def register():
#     usuario = UsuarioModel.from_json(request.get_json())
#     exists = db.session.query(UsuarioModel).filter(UsuarioModel.correo == usuario.correo).scalar() is not None

#     if exists:
#         return 'Duplicated mail', 409
#     else:
#         try:
#             db.session.add(usuario)
#             db.session.commit()
#         except Exception as error:
#             db.session.rollback()
#             return str(error), 409
#         return usuario.to_json() , 201