# -*- coding:utf-8 -*-

from flask import jsonify, make_response, request

from tools.service import Service


class ErrorService(Service):

    def __init__(self, app):
        self.app = app

    def errorhandler(self, error):
        msg = {'error': {'name': error.name,
                         'description': error.description,
                         'path': request.path}}
        self.app.logger.error('{}\n{}'.format(error, request.path))
        return make_response(jsonify(msg), error.code)

    def exceptionhandler(self, error):
        msg = {'error': {'code': 500,
                         'name': 'Internal Server Error',
                         'description': 'Not Available',
                         'path': request.path}}
        self.app.logger.error('Exception {}\n{}'.format(error, request.path))
        return make_response(jsonify(msg), 500)

    def notimplemented(self):
        msg = {'error': {'code': 501,
                         'name': 'Not Implemented Error',
                         'description': 'Not Available',
                         'path': request.path}}
        return make_response(jsonify(msg), 501)


module_name = 'tools.ErrorService'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
