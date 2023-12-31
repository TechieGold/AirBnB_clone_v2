#!/usr/bin/python3
"""
This script starts a web application containing two routes
both listening on 0.0.0.0 port=5000
"""
from flask import Flask
app = Flask(__name__)


# Routes that displays Hello HBNB!
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Routes that displays HBNB
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
