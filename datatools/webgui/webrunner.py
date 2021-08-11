# -*- coding:utf-8 -*-

import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return flask.render_template('home.html')

@app.route('/loader', methods=['GET'])
def loader():
    return 'Loader Page'

@app.errorhandler(404)
def notfound(error):
    return flask.render_template('error.html', error=error)

app.run(host='10.127.39.246', port=8081)