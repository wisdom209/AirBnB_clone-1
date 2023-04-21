#!/usr/bin/python3
""" Starts a flask app """
from flask import Flask, abort, render_template
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
    """ display c <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """ display Python  <text> """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<n>', strict_slashes=False)
def display_number_is_a_number(n):
    """display n is a number only if n is a Number"""
    try:
        n = int(n)
        return "{} is a number".format(n)
    except Exception:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def display_number_is_a_number_template(n):
    """display n is a number only if n is a Number"""
    try:
        n = int(n)
        return render_template('5-number.html', n=n)
    except Exception:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def display_number_odd_or_even_template(n):
    """display n whether odd or even"""
    try:
        n = int(n)
        if (n % 2 == 0):
            n = "{} is even".format(n)
        else:
            n = "{} is odd".format(n)
        return render_template('6-number_odd_or_even.html', n=n)
    except Exception:
        abort(404)


if __name__ == '__main__':
    """start app"""
    app.run(host='0.0.0.0', port=5000)
