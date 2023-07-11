# from .. import jwt
# from flask import jsonify
# from flask_jwt_extended import verify_jwt_in_request, get_jwt
# from functools import wraps

# def admin_required(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         verify_jwt_in_request()
#         claims = get_jwt()
#         if claims['admin'] == 1 :
#             return fn(*args, **kwargs)
#         else:
#             return 'Acceso unico para administradores', 403
#     return wrapper

# @jwt.user_identity_loader
# def user_identity_lookup(usuario):
#     return usuario.usuario_id


# #Define que atributos se guardarán dentro del token
# @jwt.additional_claims_loader
# def add_claims_to_access_token(usuario):
#     claims = {
#         'admin': usuario.admin,
#         'usuario_id': usuario.usuario_id,
#         'correo': usuario.correo,
#         "alias": usuario.alias,
#     }
#     return claims
