import flask as fl
# pip install flask


app = fl.Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return fl.render_template('basic_home.html')


@app.route('/about', methods=['POST'])
def about():
    return 'This page was made for training propouses'


@app.route('/users', methods=['GET'])
def users():
    limit = int(fl.request.args.get('limit', 10))
    return 'You will get {count} registers of users'.format(count=limit)


@app.route('/users/<string:user_name>', methods=['GET'])
def user_by_name(user_name):
    return 'Welcome {name}'.format(name=user_name)


@app.route('/users/<int:user_id>', methods=['GET'])
def user_by_id(user_id):
    return 'Welcome user #{id}'.format(id=user_id)


@app.errorhandler(404)
def not_found(error):
    return 'This page URL is not available'


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
