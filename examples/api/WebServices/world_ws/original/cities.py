from flask import request, jsonify, make_response, url_for
from tools import prepare_response, dbman


def getcities():
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
    sql = '''SELECT * FROM city ORDER BY id LIMIT %s, %s'''
    result = dbman.execute(sql, offset, limit)

    info = {}
    if len(result) > 0:
        p_url, n_url = None, None

        p_offset = 0 if offset < limit else offset - limit
        sql = '''SELECT * FROM city ORDER BY id LIMIT %s, %s'''
        if len(dbman.execute(sql, p_offset, limit)) > 0 and offset != 0:
            p_url = url_for('getcities', offset=p_offset, limit=limit, _external=True)

        sql = '''SELECT * FROM city ORDER BY id LIMIT %s, %s'''
        if len(dbman.execute(sql, offset + limit, limit)) > 0:
            n_url = url_for('getcities', offset=(offset + limit), limit=limit, _external=True)

        info = {'count': len(result), 'cities': [], 'urls': []}
        for register in result:
            cityID, name, countryCode, district, population = register

            info['cities'].append({'city_id': cityID,
                                   'name': name,
                                   'country_code': countryCode,
                                   'district': district,
                                   'population': population,
                                   'url': url_for('getcity', city_id=cityID, _external=True)})

            self_url = url_for('getcities', offset=offset, limit=limit, _external=True)
            parent_url = url_for('getworld', _external=True)
            info['urls'] = {'self': self_url, 'parent': parent_url,
                            'next': n_url, 'previous': p_url}

    dbman.disconnect()
    return prepare_response('cities.xml', info)


def getcountrycities(countrycode):
    dbman.connect()

    info = {}
    sql = '''SELECT * FROM city WHERE countrycode=%s'''
    result = dbman.execute(sql, countrycode)
    if len(result) > 0:
        p_url, n_url = None, None

        p_result = dbman.execute(sql, countrycode)
        sql = '''SELECT code FROM country WHERE code<%s ORDER BY code DESC LIMIT 1'''
        if len(p_result) == 1:
            p_url = url_for('getcountrycities', countrycode=p_result[0][0], _external=True)

        sql = '''SELECT code FROM country WHERE code>%s ORDER BY code LIMIT 1'''
        n_result = dbman.execute(sql, countrycode)
        if len(n_result) == 1:
            n_url = url_for('getcountrycities', countrycode=n_result[0][0], _external=True)

        self_url = url_for('getcountrycities', countrycode=countrycode, _external=True)
        parent_url = url_for('getcities', _external=True)
        country_url = url_for('getcountry', code=countrycode, _external=True)
        info = {'country_code': countrycode,
                'count': len(result),
                'urls': {'self': self_url, 'parent': parent_url,
                         'next': n_url, 'previous': p_url,
                         'country': country_url},
                'cities': []}
        for register in result:
            cityID, name, countryCode, district, population = register

            info['cities'].append({'city_id': cityID,
                                   'name': name,
                                   'district': district,
                                   'population': population})

    dbman.disconnect()
    return prepare_response('cities.xml', info)


def getcity(city_id):
    dbman.connect()

    info = {}
    sql = '''SELECT * FROM city WHERE id=%s LIMIT 1'''
    result = dbman.execute(sql, city_id)
    if len(result) == 1:
        register = result[0]
        cityID, name, countryCode, district, population = register

        p_url, n_url = None, None
        sql = '''SELECT id FROM city WHERE id<%s ORDER BY id DESC LIMIT 1'''
        p_result = dbman.execute(sql, city_id)
        if len(p_result) == 1:
            p_url = url_for('getcity', city_id=p_result[0][0], _external=True)

        n_result = dbman.execute(sql, city_id)
        sql = '''SELECT id FROM city WHERE id>%s ORDER BY id LIMIT 1'''
        if len(n_result) == 1:
            n_url = url_for('getcity', city_id=n_result[0][0], _external=True)

        self_url = url_for('getcity', city_id=cityID, _external=True)
        parent_url = url_for('getcities', _external=True)
        country_url = url_for('getcountry', code=countryCode, _external=True)
        info = {'urls': {'self': self_url, 'parent': parent_url,
                         'next': n_url, 'previous': p_url,
                         'country': country_url},
                'city': {'city_id': cityID,
                         'name': name,
                         'country_code': countryCode,
                         'district': district,
                         'population': population}}

    dbman.disconnect()
    return prepare_response('city.xml', info)


def postcity():
    msg = {'error': 'Content not available. Under construction'}
    return make_response(jsonify(msg), 501)


module_name = 'cities.cities'
if __name__ == '__main__':
    print('Loading {} module'.format(module_name))
else:
    print('Importing {} module'.format(module_name))
