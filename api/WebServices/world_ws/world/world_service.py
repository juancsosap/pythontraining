# -*- coding:utf-8 -*-

from flask import url_for

from tools import Service


class WorldService(Service):

    def getworld(self):
        info = {'urls': {'self': url_for('getworld', _external=True),
                         'cities': url_for('getcities', _external=True),
                         'countries': url_for('getcountries', _external=True),
                         'languages': url_for('getlanguages', _external=True)}}
        return self.prepare_response('world/world.xml', info)


module_name = 'world.WorldService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
