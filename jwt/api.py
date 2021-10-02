from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
jwt = JWTManager(app)
api = Api(app)

class AuthResource(Resource):
    def get(self):
        usuario = request.headers.get('usuario')
        if usuario in ["medico", "finanzas"]:
            access_token = create_access_token(identity=usuario)
            return jsonify(access_token=access_token)
        return 'Bad request', 403


api.add_resource(AuthResource, '/jwt')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')