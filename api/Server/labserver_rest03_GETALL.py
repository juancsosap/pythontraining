
from flask import Flask, jsonify
from jsontasks import tasks


app = Flask(__name__)


@app.route('/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
