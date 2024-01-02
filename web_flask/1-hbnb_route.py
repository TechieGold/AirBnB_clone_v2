#!/usr/bin/python3
"""
This script starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    / - display Hello HBNB!.
    /hbnb - display HBNB.
"""
from flask import Flask
app = Flask(__name__)


# Route that display Hello HBNB!
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Route that display HBNB
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
