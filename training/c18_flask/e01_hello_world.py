import flask as fl
# pip install flask


app = fl.Flask(__name__)


@app.route('/')
def home():
    return 'Hello World Home'


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
