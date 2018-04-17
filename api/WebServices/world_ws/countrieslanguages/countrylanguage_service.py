# -*- coding:utf-8 -*-

from flask import request, jsonify, url_for

from tools import Service

from countrylanguage.countrylanguage import CountryLanguage
from countrylanguage.countrylanguage_dao import CountryLanguageDAO


class CountryLanguageService(Service):

    def __init__(self):
        self.dao = CountryLanguageDAO()

    def getcountrieslanguages(self):
        try:
            limit = int(request.args.get('limit', 20))
            offset = int(request.args.get('offset', 0))
            if limit < 0:
                raise AttributeError('LIMIT must be positive')
            if offset < 0:
                raise AttributeError('OFFSET must be positive')
        except Exception:
            return self.make_response(jsonify({'error': 'Invalid Filters'}), 400)

        results = self.dao.retrive_all(offset, limit)

        info = {}
        if len(results) > 0:
            p_url, n_url = None, None

            p_offset = 0 if offset < limit else offset - limit
            if len(self.dao.retrive_all(p_offset, limit)) > 0 and offset != 0:
                p_url = url_for('getcountrieslanguages', offset=p_offset,
                                limit=limit, _external=True)

            n_offset = offset + limit
            if len(self.dao.retrive_all(n_offset, limit)) > 0:
                n_url = url_for('getcountrieslanguages', offset=n_offset,
                                limit=limit, _external=True)

            info = {'count': len(results), 'countrylanguage': [], 'urls': []}
            for city in results:
                info['cities'].append({'city_id': city.city_id,
                                       'name': city.name,
                                       'country_code': city.country_code,
                                       'district': city.district,
                                       'population': city.population,
                                       'url': url_for('getcity', city_id=city.city_id, _external=True)})

            self_url = url_for('getcountrieslanguages', offset=offset, limit=limit, _external=True)
            parent_url = url_for('getworld', _external=True)
            info['urls'] = {'self': self_url, 'parent': parent_url,
                            'next': n_url, 'previous': p_url}

        return self.prepare_response('countrieslanguages/countrieslanguages.xml', info)

    def getcountrylanguage(self, country_code):
        info = {}
        countrylanguage = self.dao.retrive(CountryLanguage(country_code))
        if countrylanguage:
            p_url, n_url = None, None

            p_countrylanguage = self.dao.retrive_previous(CountryLanguage(country_code))
            if p_countrylanguage:
                p_url = url_for('getcountrylanguages',
                                country_code=p_countrylanguages.country_code, _external=True)

            n_countrylanguages = self.dao.retrive_next(CountryLanguage(country_code))
            if n_countrylanguages:
                n_url = url_for('getcountrylanguages',
                                country_code=n_countrylanguages.country_code, _external=True)

            self_url = url_for('getcountrylanguages', country_code=country_code, _external=True)
            parent_url = url_for('getcountrieslanguages', _external=True)
            country_url = url_for('getcountry', code=countrylanguage.country_code, _external=True)
            info = {'urls': {'self': self_url, 'parent': parent_url,
                             'next': n_url, 'previous': p_url,
                             'country': country_url},
                    'city': {'city_id': city.city_id,
                             'name': city.name,
                             'country_code': city.country_code,
                             'district': city.district,
                             'population': city.population}}

            return self.prepare_response('countrieslanguages/countrylanguages.xml', info)


module_name = 'countrieslanguages.CountryLanguageService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
