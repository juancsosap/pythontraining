from flask import json, make_response


class VehiculoService:
    def getAll(self):
        return 'All Vehiculos'

    def post(self, patente):
        return 'Creating Vehiculo: ' + patente

    def get(self, patente):
        msg = json.dumps({"patente": patente})
        response = make_response(msg)
        response.headers['Content-Type'] = 'application/json'
        return response

    def put(self, patente):
        return 'Updating Vehiculo: ' + patente

    def delete(self, patente):
        return 'Deleting Vehiculo: ' + patente
