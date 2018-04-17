from tools import prepare_response
from flask import url_for


def getworld():
    info = {'urls': {'self': url_for('getworld', _external=True),
                     'cities': url_for('getcities', _external=True),
                     'countries': url_for('getcountries', _external=True),
                     'countrieslanguages': url_for('getcountrieslanguages', _external=True)}}
    return prepare_response('world.xml', info)


module_name = 'world.world'
if __name__ == '__main__':
    print('Loading {} module'.format(module_name))
else:
    print('Importing {} module'.format(module_name))
