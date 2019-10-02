# -*- coding:utf-8 -*-


from flask import request, json, render_template, make_response, abort, url_for

from tools import DAO


class Service:

    @classmethod
    def xmlify(cls, template, value):
        text = render_template(template, value=value)
        response = make_response(text)
        response.headers['Content-Type'] = 'application/xml'
        return response

    @classmethod
    def jsonify(cls, value):
        text = json.dumps(value)
        response = make_response(text)
        response.headers['Content-Type'] = 'application/json'
        return response

    @classmethod
    def prepare_response(cls, template, info):
        if len(info) > 0:
            formats = ['application/json', 'application/xml']
            accept = request.accept_mimetypes.best_match(formats)
            if accept == 'application/xml':
                return cls.xmlify(template, info)
            else:
                return cls.jsonify(info)

        return make_response(cls.jsonify({}), 204)


module_name = 'tools.Service'
if __name__ == '__main__':
    print('Loading {} class'.format(module_name))
else:
    print('Importing {} class'.format(module_name))
