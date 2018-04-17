# -*- coding:utf-8 -*-

from flask import request, jsonify, url_for

from tools import Service

from countries.country import Country
from countries.country_dao import CountryDAO


class CountryService(Service):

    def __init__(self):
        self.dao = CountryDAO()

    def getcountries(self):
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
                p_url = url_for('getcountries', offset=p_offset, limit=limit, _external=True)

            n_offset = offset + limit
            if len(self.dao.retrive_all(n_offset, limit)) > 0:
                n_url = url_for('getcountries', offset=n_offset, limit=limit, _external=True)

            info = {'count': len(results), 'countries': [], 'urls': []}
            for country in results:
                url = url_for('getcountry', country_code=country.country_code, _external=True)
                info['countries'].append({'country_code': country.country_code,
                                          'name': country.name,
                                          'continent': country.continent,
                                          'region': country.region,
                                          'surface_area': country.surface_area,
                                          'independent_year': country.independent_year,
                                          'population': country.population,
                                          'life_expectation': country.life_expectation,
                                          'gnp': country.gnp,
                                          'gnp_old': country.gnp_old,
                                          'local_name': country.local_name,
                                          'government_form': country.government_form,
                                          'head_of_state': country.head_of_state,
                                          'capital': country.capital,
                                          'code2': country.code2,
                                          'url': url})

            self_url = url_for('getcountries', offset=offset, limit=limit, _external=True)
            parent_url = url_for('getworld', _external=True)
            info['urls'] = {'self': self_url, 'parent': parent_url,
                            'next': n_url, 'previous': p_url}

        return self.prepare_response('countries/countries.xml', info)

    def getcountry(self, country_code):
        info = {}
        country = self.dao.retrive(Country(country_code))
        if country:
            p_url, n_url = None, None

            p_country = self.dao.retrive_previous(Country(country_code))
            if p_country:
                p_url = url_for('getcountry', country_code=p_country.country_code, _external=True)

            n_country = self.dao.retrive_next(Country(country_code))
            if n_country:
                n_url = url_for('getcountry', country_code=n_country.country_code, _external=True)

            self_url = url_for('getcountry', country_code=country_code, _external=True)
            parent_url = url_for('getcountries', _external=True)
            info = {'urls': {'self': self_url, 'parent': parent_url,
                             'next': n_url, 'previous': p_url},
                    'country': {'country_code': country.country_code,
                                'name': country.name,
                                'continent': country.continent,
                                'region': country.region,
                                'surface_area': country.surface_area,
                                'independent_year': country.independent_year,
                                'population': country.population,
                                'life_expectation': country.life_expectation,
                                'gnp': country.gnp,
                                'gnp_old': country.gnp_old,
                                'local_name': country.local_name,
                                'government_form': country.government_form,
                                'head_of_state': country.head_of_state,
                                'capital': country.capital,
                                'code2': country.code2}}

            return self.prepare_response('countries/country.xml', info)


module_name = 'countries.CountryService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
