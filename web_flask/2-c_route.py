#!/usr/bin/python3
""" Starts a flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display_hellohbnb():
    """ display Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ display HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_is_text(text):
    """ display c is <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    """start app"""
    app.run(host='0.0.0.0', port=5000)
