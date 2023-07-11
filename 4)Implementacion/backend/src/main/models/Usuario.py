# class Usuario:
#     def __init__(self, _id, correo, alias, nombre, password, descripcion, foto, seguidores, seguidos, admin):
#         self._id = _id
#         self.correo = correo
#         self.alias = alias
#         self.nombre = nombre
#         self.password = password
#         self.descripcion = descripcion
#         self.foto = foto
#         self.seguidores = seguidores 
#         self.seguidos = seguidos
#         self.admin = admin  

#     # #! De objeto a json
#     # def to_json_usuario(self):
#     #     poemas = [poema.to_json() for poema in self.poemas]
#     #     json_str = {
#     #         'alias':self.alias,
#     #         'poemas':poemas
#     #     }
#     #     return json_str
    

#     #! Crea una instancia de la clase Usuario desde un json. 
#     #! @staticmethod indica que el metodo pertenece a la clase y no a una instancia.
#     @staticmethod
#     def from_json(json_str):
#         _id = json_str.get('_id')
#         correo = json_str.get('correo')
#         alias = json_str.get('alias')
#         nombre = json_str.get('nombre')
#         password = json_str.get('password')
#         descripcion = json_str.get('descripcion')
#         foto = json_str.get("foto")
#         seguidores = json_str.get("seguidores") 
#         seguidos = json_str.get("seguidos") 
#         admin = json_str.get("admin")   
        
#         return Usuario(
#             _id = _id,
#             correo = correo,
#             alias = alias,
#             nombre = nombre,
#             password = password,
#             descripcion = descripcion,
#             foto = foto,
#             seguidores = seguidores, 
#             seguidos = seguidos,
#             admin = admin  
#         )