from flask import json, make_response, request
from dao import PersonaDAO
from model import Persona, Rut


class PersonaService:
    def __init__(self):
        self.dao = PersonaDAO()

    def getAll(self):
        personas = self.dao.retrive_all()
        msg = json.dumps({"personas": [self.topersonadict(persona) for persona in personas]})
        response = make_response(msg)
        response.headers['Content-Type'] = 'application/json'
        return response

    def post(self):
        data = json.loads(request.json)
        persona = self.dao.create(Persona(data['nombre'], data['apellido'], Rut(data['rut'])))
        msg = json.dumps(self.topersonadict(persona))
        response = make_response(msg)
        response.headers['Content-Type'] = 'application/json'
        return response

    def get(self, id):
        persona = self.dao.retrive(Persona(id=id))
        msg = json.dumps(self.topersonadict(persona))
        response = make_response(msg)
        response.headers['Content-Type'] = 'application/json'
        return response

    def put(self, id):
        return 'Updating Persona: ' + id

    def delete(self, id):
        persona = self.dao.delete(Persona(id=id))
        msg = json.dumps(self.topersonadict(persona))
        response = make_response(msg)
        response.headers['Content-Type'] = 'application/json'
        return response

    @staticmethod
    def topersonadict(persona):
        persona_dict = {"id": persona.id,
                        "rut": persona.rut,
                        "nombre": persona.nombre,
                        "apellido": persona.apellido}
        return persona_dict
