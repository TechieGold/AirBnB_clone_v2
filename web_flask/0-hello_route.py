#!/usr/bin/python3
""" This script starts a flask application listening on 0.0.0.0 port 500 """

from flask import Flask
app = Flask(__name__)


# Routes that displays Hello HBNB!
@app.route('/', strict_slashes=False)
def hell0():
    return 'Hello HBNB!'


# Run the Flask application if this file is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
