from flask import request, jsonify, make_response, url_for
from tools import prepare_response, dbman


def getcountrieslanguages():
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
    sql = '''SELECT * FROM countrylanguage ORDER BY countrycode LIMIT %s, %s'''
    result = dbman.execute(sql, offset, limit)

    info = {}
    if len(result) > 0:
        p_url, n_url = None, None

        p_offset = 0 if offset < limit else offset - limit
        sql = '''SELECT * FROM countrylanguage ORDER BY countrycode LIMIT %s, %s'''
        if len(dbman.execute(sql, p_offset, limit)) > 0 and offset != 0:
            p_url = url_for('getcountrieslanguages', offset=p_offset, limit=limit, _external=True)

        n_offset = offset + limit
        sql = '''SELECT * FROM countrylanguage ORDER BY countrycode LIMIT %s, %s'''
        if len(dbman.execute(sql, n_offset, limit)) > 0:
            n_url = url_for('getcountrieslanguages', offset=n_offset, limit=limit, _external=True)

        info = {'count': len(result), 'countries': {}, 'urls': []}
        for register in result:
            countrycode, language, is_official, percentage = register

            if countrycode not in info['countries'].keys():
                url = url_for('getcountrylanguages', countrycode=countrycode, _external=True)
                info['countries'][countrycode] = {'languages': [], 'url': url}

            info['countries'][countrycode]['languages'].append({
                'language': language,
                'is_official': is_official,
                'percentage': percentage, })

        self_url = url_for('getcountrieslanguages', offset=offset, limit=limit, _external=True)
        parent_url = url_for('getworld', _external=True)
        info['urls'] = {'self': self_url, 'parent': parent_url,
                        'next': n_url, 'previous': p_url}

    dbman.disconnect()
    return prepare_response('countrieslanguages.xml', info)


def getcountrylanguages(countrycode):
    dbman.connect()

    info = {}
    sql = 'SELECT * FROM countrylanguage WHERE countrycode=%s'
    result = dbman.execute(sql, countrycode)
    if len(result) > 0:
        p_url, n_url = None, None

        p_result = dbman.execute(sql, countrycode)
        sql = '''SELECT countrycode FROM countrylanguage WHERE countrycode<%s
                 ORDER BY countrycode DESC LIMIT 1'''
        if len(p_result) == 1:
            p_url = url_for('getcountrylanguages', countrycode=p_result[0][0], _external=True)

        sql = '''SELECT countrycode FROM countrylanguage
                 WHERE countrycode>%s ORDER BY countrycode LIMIT 1'''
        n_result = dbman.execute(sql, countrycode)
        if len(n_result) == 1:
            n_url = url_for('getcountrylanguages', countrycode=n_result[0][0], _external=True)

        self_url = url_for('getcountrylanguages', countrycode=countrycode, _external=True)
        parent_url = url_for('getcountrieslanguages', _external=True)
        country_url = url_for('getcountry', code=countrycode, _external=True)
        info = {'urls': {'self': self_url, 'parent': parent_url,
                         'next': n_url, 'previous': p_url,
                         'country': country_url},
                'country_code': countrycode,
                'count': len(result),
                'languages': []}

        for register in result:
            countrycode, language, is_official, percentage = register
            info['languages'].append(
                {'language': language,
                 'is_official': is_official,
                 'percentage': percentage, })

    dbman.disconnect()
    return prepare_response('countrylanguages.xml', info)


module_name = 'countrieslanguages.countrieslanguages'
if __name__ == '__main__':
    print('Loading {} module'.format(module_name))
else:
    print('Importing {} module'.format(module_name))
