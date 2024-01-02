#!/usr/bin/python3
"""
This script starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    / - display Hello HBNB!.
    /hbnb - display HBNB.
    /c/<text> - display C followed by the value of text variable.
    /python - display Python followed by the value of text variable.
    /number/<int:n> - display “n is a number” only if n is an integer.
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


#  Route that display Python followed by the value of text variable
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python {}" .format(text.replace("_", " "))


# Route that display “n is a number” only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return "{} is a number".format(n)


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
