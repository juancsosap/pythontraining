import model

from flask import Flask

from service import HomeService, PersonaService, VehiculoService

app = Flask(__name__)

home_service = HomeService()
persona_service = PersonaService()
vehiculo_service = VehiculoService()


@app.route('/api/', methods=['GET'])
def getapihome():
    return home_service.get()


@app.route('/api/vehiculos', methods=['GET'])
def getvehiculos():
    return vehiculo_service.getAll()


@app.route('/api/vehiculos/<string:patente>', methods=['GET'])
def getvehiculo(patente):
    return vehiculo_service.get(patente)


@app.route('/api/vehiculos/<string:patente>', methods=['POST'])
def postvehiculo(patente):
    return vehiculo_service.post(patente)


@app.route('/api/vehiculos/<string:patente>', methods=['PUT'])
def putvehiculo(patente):
    return vehiculo_service.put(patente)


@app.route('/api/vehiculos/<string:patente>', methods=['DELETE'])
def deletevehiculo(patente):
    return vehiculo_service.delete(patente)


@app.route('/api/personas', methods=['GET'])
def getpersonas():
    return persona_service.getAll()


@app.route('/api/personas', methods=['POST'])
def postpersona():
    return persona_service.post()


@app.route('/api/personas/<int:id>', methods=['GET'])
def getpersona(id):
    return persona_service.get(id)


@app.route('/api/personas/<int:id>', methods=['PUT'])
def putpersona(id):
    return persona_service.put(id)


@app.route('/api/personas/<int:id>', methods=['DELETE'])
def deletepersona(id):
    return persona_service.delete(id)


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
