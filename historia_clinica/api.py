import requests
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, current_user


class HistoriaClinicaDetail(Resource):
    @jwt_required()
    def get(self, historia_clinica_id):
        if current_user == 'medico':
            return f'datos de historia clínica {historia_clinica_id}'
        return 'No tiene los permisos necesarios para acceder a este recurso', 403
