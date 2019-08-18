import flask as fl
# pip install flask


app = fl.Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return 'Hello World Home'


@app.route('/about', methods=['POST'])
def about():
    return 'This page was made for training propouses'


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
