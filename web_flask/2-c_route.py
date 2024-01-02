#!/usr/bin/python3
"""
This script starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    / - display Hello HBNB!.
    /hbnb - display HBNB.
    /c/<text> - display C followed by the value of text variable.
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


# Route that display C followed by the value of text variable
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return "C {}" .format(text.replace("_", " "))


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
