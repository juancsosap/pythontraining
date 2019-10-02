import flask as fl
# pip install flask

from flask import request
import json

users_list = set(['juan', 'luis', 'pepe'])


app = fl.Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    return fl.render_template('home.html')


@app.route('/about', methods=['GET'])
def about():
    return fl.render_template('about.html')


@app.route('/users', methods=['GET'])
def users():
    limit = int(fl.request.args.get('limit', 10))
    return 'You will get {count} registers of users'.format(count=limit)


@app.route('/users', methods=['POST'])
def create_user():
    user = request.form['user']
    users_list.add(user)
    print(users_list)
    return 'User {user} created'.format(user=user)


@app.route('/users/<string:user_name>', methods=['GET'])
def user_by_name(user_name):
    if(user_name not in users_list):
        fl.abort(400)
    else:
        return fl.render_template('user_by_name.html', name=user_name.capitalize())


@app.route('/users/<int:user_id>', methods=['GET'])
def user_by_id(user_id):
    return 'Welcome user #{id}'.format(id=user_id)


@app.errorhandler(400)
@app.errorhandler(404)
def not_found(error):
    return fl.render_template('error.html')


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
