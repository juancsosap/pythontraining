from flask import Flask, jsonify, request, render_template, make_response
from datetime import datetime
from math import pi

app = Flask(__name__)
formats = ['application/json', 'application/xml']


@app.route('/api/v1/CurrentTime', methods=['GET'])
def get_time():
    return render_result(datetime.now(), 'CurrentTimeResponse')


@app.route('/api/v1/pi', methods=['GET'])
def get_pi():
    return render_result(pi, 'NumberResponse')


def render_result(value, dato):
    accept = request.accept_mimetypes.best_match(formats)
    if accept == 'application/json':
        return jsonify({dato: str(value)})
    else:
        text = render_template('GenericValueResponse.xml', dato=dato, value=value)
        response = make_response(text)
        response.headers["Content-Type"] = "application/xml"
        return response


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
