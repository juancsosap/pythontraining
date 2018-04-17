# -*- coding:utf-8 -*-

from flask import Flask

from tools import ErrorService
from world.world_service import WorldService
from cities.city_service import CityService
from countries.country_service import CountryService

app = Flask(__name__)

error_service = ErrorService(app)

world_service = WorldService()
city_service = CityService()
country_service = CountryService()


@app.errorhandler(404)
@app.errorhandler(500)
def errorhandler(e):
    return error_service.errorhandler(e)


@app.errorhandler(Exception)
def exceptionhandler(e):
    return error_service.exceptionhandler(e)


@app.route('/api/world', methods=['GET'])
def getworld():
    return world_service.getworld()


@app.route('/api/world/cities', methods=['GET'])
def getcities():
    return city_service.getcities()


@app.route('/api/world/cities/<int:city_id>', methods=['GET'])
def getcity(city_id):
    return city_service.getcity(city_id)


@app.route('/api/world/countries', methods=['GET'])
def getcountries():
    return country_service.getcountries()


@app.route('/api/world/countries/<string:country_code>', methods=['GET'])
def getcountry(country_code):
    return country_service.getcountry(country_code)


@app.route('/api/world/countries/<string:country_code>/cities', methods=['GET'])
def getcountrycities(country_code):
    return error_service.notimplemented()


@app.route('/api/world/countries/<string:country_code>/languages', methods=['GET'])
def getcountrylanguages(country_code):
    return error_service.notimplemented()


@app.route('/api/world/languages', methods=['GET'])
def getlanguages():
    return error_service.notimplemented()


@app.route('/api/world/languages/<string:language>', methods=['GET'])
def getlanguage(language):
    return error_service.notimplemented()


module_name = 'app'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
    app.run(host='localhost', port=80, debug=True)
else:
    print('Importing {} module'.format(module_name))
