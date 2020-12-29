import flask
import main

app = flask.Flask(__name__)

@app.route('/convert')
def convert():
    return main.convert_temp(flask.request)
