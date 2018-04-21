import flask as fl
# pip install flask

users_list = ['juan', 'luis', 'pepe']


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
    if(len(users_list) > limit):
        users_temp_list = users_list[:limit]
    else:
        users_temp_list = users_list
    return fl.render_template('users.html', users=users_temp_list)


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
