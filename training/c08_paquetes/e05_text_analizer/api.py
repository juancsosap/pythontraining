import flask
import textanalizer as ta

app = flask.Flask(__name__)

@app.route('/fill', methods=['GET'])
def fill():
    return flask.render_template('fill_data.html')

@app.route('/text', methods=['GET'])
def analize():
    text = flask.request.args.get('text', '')
    data = analize(text)
    return flask.render_template('text_analizer.html', data=data)

def analize(text):
    top_words = ta.top(text, 10)
    top_chars = ta.top(text, 10, chars=True)
    return {'text':text, 'top_words':top_words, 'top_chars':top_chars}

if __name__ == "__main__":
    app.run(host='localhost', port=80, debug=True)