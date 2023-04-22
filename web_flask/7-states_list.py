#!/usr/bin/python3
"""Script that starts a Flask app"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """list the state elements"""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(e):
    """remove the currentSQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
