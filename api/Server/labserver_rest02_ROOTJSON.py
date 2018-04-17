from flask import Flask, jsonify
# pip install flask

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'Hello World!'})


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
