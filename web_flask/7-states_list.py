#!/usr/bin/python3
"""
This script starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""

from flask import Flask, render_template
from models import storage
from models.state import state
app = Flask(__name__)
app.url_map.strict_slashes = False


#  This route close the current SQLAlchemy Session
@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


# This route displays a HTML page with a list of all state
# storage in DBstorage.
@app.route('/state_list')
def state_list():
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run('0.0.0.0', port=50000)
    app.run(debug=True)
