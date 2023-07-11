# import os
# from flask import Flask
# from dotenv import load_dotenv
# from flask_restful import Api
# from flask_jwt_extended import JWTManager

# api = Api()
# jwt = JWTManager()

# def create_app():
# 	app = Flask(__name__)
# 	load_dotenv()

# 	# import main.resources as resources
# 	# api.add_resource(resources.PoemaResource, '/poema/<poema_id>')
	
# 	api.init_app(app)
	
# 	app.config['PROPAGATE_EXCEPTIONS'] = True
# 	app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
# 	app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
# 	jwt.init_app(app)

# 	from main.auth import routes
# 	app.register_blueprint(routes.auth)

# 	return app