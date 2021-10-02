from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
import requests
from flask_jwt_extended import JWTManager
from api import HistoriaClinicaDetail


app = Flask(__name__)
ma = Marshmallow(app)
app.config["JWT_SECRET_KEY"] = "secret-jwt"  # Change this!
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False

jwt = JWTManager(app)
api = Api(app)


@jwt.user_lookup_loader
def get_logged_user(jwt_header, jwt_data):
    identity = jwt_data['sub']
    return identity


api.add_resource(HistoriaClinicaDetail, '/historia_clinica/<int:historia_clinica_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')