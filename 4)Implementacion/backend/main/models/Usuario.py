from .. import mongo

class Usuario:
    def __init__(self, correo, alias, nombre, password, descripcion, foto, seguidores, seguidos, admin):
        self.correo = correo
        self.alias = alias
        self.nombre = nombre
        self.password = password
        self.descripcion = descripcion
        self.foto = foto
        self.seguidores = seguidores 
        self.seguidos = seguidos
        self.admin = admin  

    # def save(self):
    #     # Aquí puedes usar las funciones de la biblioteca flask_pymongo para guardar el usuario en la base de datos
    #     mongo.db.users.insert_one(self.__dict__)

    # @staticmethod
    # def find_by_correo(correo):
    #     # Aquí puedes usar las funciones de la biblioteca flask_pymongo para buscar un usuario por correo en la base de datos
    #     # Ejemplo: mongo.db.users.find_one({'correo': correo})
    #     return mongo.db.users.find_one({"correo": correo})


    # @staticmethod
    # def find_by_id(user_id):
    #     # Aquí puedes usar las funciones de la biblioteca flask_pymongo para buscar un usuario por ID en la base de datos
    #     return mongo.db.users.find_one({'_id': ObjectId(user_id)})

    # @staticmethod
    # def find_all():
    #     # Aquí puedes usar las funciones de la biblioteca flask_pymongo para obtener todos los usuarios de la base de datos
    #     return mongo.db.users.find()

    # def update(self):
    #     # Aquí puedes usar las funciones de la biblioteca flask_pymongo para actualizar el usuario en la base de datos
    #     mongo.db.users.update_one({'_id': ObjectId(self.id)}, {'$set': self.__dict__})

    def to_json(self):
        return  {
        "correo": self.correo ,
        "alias": self.alias ,
        "nombre": self.nombre,
        "password": self.password,
        "descripcion" : self.descripcion,
        "foto": self.foto,
        "seguidores": self.seguidores,
        "seguidos": self.seguidos,
        "admin": self.admin,
        }
    

    #! Crea una instancia de la clase Usuario desde un json. 
    #! @staticmethod indica que el metodo pertenece a la clase y no a una instancia.
    @staticmethod
    def from_json(json_str):
        correo = json_str.get('correo')
        alias = json_str.get('alias')
        nombre = json_str.get('nombre')
        password = json_str.get('password')
        descripcion = json_str.get('descripcion')
        foto = json_str.get("foto")
        seguidores = json_str.get("seguidores") 
        seguidos = json_str.get("seguidos") 
        admin = json_str.get("admin")   
        
        return Usuario(
            correo = correo,
            alias = alias,
            nombre = nombre,
            password = password,
            descripcion = descripcion,
            foto = foto,
            seguidores = seguidores, 
            seguidos = seguidos,
            admin = admin  
        )


