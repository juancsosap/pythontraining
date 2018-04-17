from flask import request, jsonify, make_response, url_for
from tools import prepare_response, dbman


def getcountries():
    dbman.connect()
    try:
        limit = int(request.args.get('limit', 20))
        offset = int(request.args.get('offset', 0))
        if limit < 0:
            raise AttributeError('LIMIT must be positive')
        if offset < 0:
            raise AttributeError('OFFSET must be positive')
    except Exception:
        return make_response(jsonify({'error': 'Invalid Filters'}), 400)
    sql = '''SELECT * FROM country ORDER BY code LIMIT %s, %s'''
    result = dbman.execute(sql, offset, limit)

    info = {}
    if len(result) > 0:
        p_url, n_url = None, None

        sql = '''SELECT * FROM country ORDER BY code LIMIT %s, %s'''
        p_offset = 0 if offset < limit else offset - limit
        if len(dbman.execute(sql, p_offset, limit)) > 0 and offset != 0:
            p_url = url_for('getcountries', offset=p_offset, limit=limit, _external=True)

        sql = '''SELECT * FROM country ORDER BY code LIMIT %s, %s'''
        if len(dbman.execute(sql, offset + limit, limit)) > 0:
            n_url = url_for('getcountries', offset=(offset + limit), limit=limit, _external=True)

        info = {'count': len(result), 'countries': [], 'urls': []}
        for register in result:
            code, name, continent, region, surface_area, independent_day, \
                population, life_expectation, gnp, gnp_old, local_name, \
                government_form, head_of_state, capital, code2 = register

            info['countries'].append({'code': code,
                                      'name': name,
                                      'continent': continent,
                                      'region': region,
                                      'surface_area': surface_area,
                                      'independent_day': independent_day,
                                      'population': population,
                                      'life_expectation': life_expectation,
                                      'gnp': gnp,
                                      'gnp_old': gnp_old,
                                      'local_name': local_name,
                                      'government_form': government_form,
                                      'head_of_state': head_of_state,
                                      'capital': capital,
                                      'code2': code2,
                                      'url': url_for('getcountry', code=code, _external=True)})

        self_url = url_for('getcountries', offset=offset, limit=limit, _external=True)
        parent_url = url_for('getworld', _external=True)
        info['urls'] = {'self': self_url, 'parent': parent_url, 'next': n_url, 'previous': p_url}

    dbman.disconnect()
    return prepare_response('countries.xml', info)


def getcountry(code):
    dbman.connect()

    info = {}
    sql = '''SELECT * FROM country WHERE code=%s LIMIT 1'''
    result = dbman.execute(sql, code)
    if len(result) == 1:
        register = result[0]
        code, name, continent, region, surface_area, independent_day, \
            population, life_expectation, gnp, gnp_old, local_name, \
            government_form, head_of_state, capital, code2 = register

        p_url, n_url = None, None

        p_result = dbman.execute(sql, code)
        sql = '''SELECT code FROM country WHERE code<%s ORDER BY code DESC LIMIT 1'''
        if len(p_result) == 1:
            p_url = url_for('getcountry', code=p_result[0][0], _external=True)

        sql = '''SELECT code FROM country WHERE code>%s ORDER BY code LIMIT 1'''
        n_result = dbman.execute(sql, code)
        if len(n_result) == 1:
            n_url = url_for('getcountry', code=n_result[0][0], _external=True)

        self_url = url_for('getcountry', code=code, _external=True)
        parent_url = url_for('getcountries', _external=True)
        cities_url = url_for('getcountrycities', countrycode=code, _external=True)
        languages_url = url_for('getcountrylanguages', countrycode=code, _external=True)
        info = {'urls': {'self': self_url, 'parent': parent_url,
                         'next': n_url, 'previous': p_url,
                         'cities': cities_url, 'languages': languages_url},
                'country': {'code': code,
                            'name': name,
                            'continent': continent,
                            'region': region,
                            'surface_area': surface_area,
                            'independent_day': independent_day,
                            'population': population,
                            'life_expectation': life_expectation,
                            'gnp': gnp,
                            'gnp_old': gnp_old,
                            'local_name': local_name,
                            'government_form': government_form,
                            'head_of_state': head_of_state,
                            'capital': capital,
                            'code2': code2}}

    dbman.disconnect()
    return prepare_response('country.xml', info)


module_name = 'countries.countries'
if __name__ == '__main__':
    print('Loading {} module'.format(module_name))
else:
    print('Importing {} module'.format(module_name))
