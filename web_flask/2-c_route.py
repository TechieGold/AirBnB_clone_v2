#!/usr/bin/python3
"""
This script starts a web application containing three routes
all listening on 0.0.0.0 port=5000
"""
from flask import Flask
app = Flask(__name__)


# Route that displays Hello HBNB!
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


# Route that displays HBNB
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


# Route that display C followed by the value of text variable
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}" .format(text.replace("_", " "))


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
