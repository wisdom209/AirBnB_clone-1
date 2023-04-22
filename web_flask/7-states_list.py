#!/usr/bin/python3
""" Script that starts flask web application """
from models import *
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/state_list', strict_slashes=False)
def get_state_list():
    """function defines the /state_list route"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_database(exception):
    """tear down db"""
    storage.close()


if __name__ == '__main__':
    """run the app"""
    app.run(host='0.0.0.0', port='5000')
