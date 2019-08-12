# -*- coding:utf-8 -*-

from flask import request, jsonify, url_for, make_response

from tools import Service

from cities.city import City
from cities.city_dao import CityDAO


class CityService(Service):

    def __init__(self):
        self.dao = CityDAO()

    def getcities(self):
        try:
            limit = int(request.args.get('limit', 20))
            offset = int(request.args.get('offset', 0))
            if limit < 0:
                raise AttributeError('LIMIT must be positive')
            if offset < 0:
                raise AttributeError('OFFSET must be positive')
        except Exception:
            return make_response(jsonify({'error': 'Invalid Filters'}), 400)

        results = self.dao.retrive_all(offset, limit)

        info = {}
        if len(results) > 0:
            p_url, n_url = None, None

            p_offset = 0 if offset < limit else offset - limit
            if len(self.dao.retrive_all(p_offset, limit)) > 0 and offset != 0:
                p_url = url_for('getcities', offset=p_offset, limit=limit, _external=True)

            n_offset = offset + limit
            if len(self.dao.retrive_all(n_offset, limit)) > 0:
                n_url = url_for('getcities', offset=n_offset, limit=limit, _external=True)

            info = {'count': len(results), 'cities': [], 'urls': []}
            for city in results:
                info['cities'].append({'city_id': city.city_id,
                                       'name': city.name,
                                       'country_code': city.country_code,
                                       'district': city.district,
                                       'population': city.population,
                                       'url': url_for('getcity', city_id=city.city_id, _external=True)})

            self_url = url_for('getcities', offset=offset, limit=limit, _external=True)
            parent_url = url_for('getworld', _external=True)
            info['urls'] = {'self': self_url, 'parent': parent_url,
                            'next': n_url, 'previous': p_url}

        return self.prepare_response('cities/cities.xml', info)

    def getcity(self, city_id):
        info = {}
        city = self.dao.retrive(City(city_id))
        if city:
            p_url, n_url = None, None

            p_city = self.dao.retrive_previous(City(city_id))
            if p_city:
                p_url = url_for('getcity', city_id=p_city.city_id, _external=True)

            n_city = self.dao.retrive_next(City(city_id))
            if n_city:
                n_url = url_for('getcity', city_id=n_city.city_id, _external=True)

            self_url = url_for('getcity', city_id=city_id, _external=True)
            parent_url = url_for('getcities', _external=True)
            country_url = url_for('getcountry', country_code=city.country_code, _external=True)
            info = {'urls': {'self': self_url, 'parent': parent_url,
                             'next': n_url, 'previous': p_url,
                             'country': country_url},
                    'city': {'city_id': city.city_id,
                             'name': city.name,
                             'country_code': city.country_code,
                             'district': city.district,
                             'population': city.population}}

            return self.prepare_response('cities/city.xml', info)


module_name = 'cities.CityService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
