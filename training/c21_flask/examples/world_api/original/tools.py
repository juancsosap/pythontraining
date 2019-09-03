import pymysql

from flask import request, jsonify, render_template, make_response, abort


def xmlify(template, value):
    text = render_template(template, value=value)
    response = make_response(text)
    response.headers['Content-Type'] = 'application/xml'
    return response


def prepare_response(template, info):
    if len(info) > 0:
        formats = ['application/json', 'application/xml']
        accept = request.accept_mimetypes.best_match(formats)
        if accept == 'application/json':
            return jsonify(info)
        elif accept == 'application/xml':
            return xmlify(template, info)
        else:
            abort(406)
    return make_response(jsonify({}), 204)


class MySQLDBManager:

    def __init__(self, **kwargs):
        self.host = kwargs['host'] if 'host' in kwargs else 'localhost'
        self.port = kwargs['port'] if 'port' in kwargs else 3306
        self.user = kwargs['user'] if 'user' in kwargs else 'root'
        self.password = kwargs['password']
        self.db = kwargs['db']

    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    db=self.db,
                                    user=self.user,
                                    password=self.password)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute(self, sql, *args):
        if len(args) > 0:
            self.cursor.execute(sql, args)
        else:
            self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


dbman = MySQLDBManager(password='roottoor', db='world')

module_name = 'tools.tools'
if __name__ == '__main__':
    print('Loading {} module'.format(module_name))
else:
    print('Importing {} module'.format(module_name))
