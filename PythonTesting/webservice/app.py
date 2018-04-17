# -*- coding:utf-8 -*-

from flask import Flask

from service import BasicService

app = Flask(__name__)

service = BasicService()


@app.route('/api/v1/basic/infos', methods=['GET'])
def getinfos():
    return service.getinfos()


@app.route('/api/v1/basic/infos', methods=['POST'])
def postinfo():
    return service.getinfo(id)


@app.route('/api/v1/basic/infos/<int:id>', methods=['GET'])
def getinfo(id):
    return service.getinfo(id)


@app.route('/api/v1/basic/infos/<int:id>', methods=['PUT'])
def putinfo(id):
    return service.putinfo(id)


@app.route('/api/v1/basic/infos/<int:id>', methods=['DELETE'])
def deleteinfo(id):
    return service.deleteinfo(id)


module_name = 'app'
if __name__ == '__main__':
    print('Loading {} module'.format(module_name))
    app.run(host='localhost', port=80, debug=True)
else:
    print('Importing {} module'.format(module_name))
