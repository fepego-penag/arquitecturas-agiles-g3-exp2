import requests
from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, current_user


class ReporteDetail(Resource):
    @jwt_required()
    def get(self, reporte_id):
        if current_user == 'finanzas':
            return f'procesando reporte {reporte_id}'
        return 'No tiene los permisos necesarios para acceder a este recurso', 403    
