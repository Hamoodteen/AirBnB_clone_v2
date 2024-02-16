#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttttttttt"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hellohbnb():
    """commenttttttttttttttttttttttttttttttttttttt"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """commenttttttttttttttttttttttttttttttttttttt"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text="is cool"):
    """commenttttttttttttttttttttttttttttttttttttt"""
    formatted = text.replace('_', ' ')
    return f'C {formatted}'


@app.route('/python/<text>', strict_slashes=False)
def py_text(text="is cool"):
    """commenttttttttttttttttttttttttttttttttttttt"""
    formatted = text.replace('_', ' ')
    return f'Python {formatted}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
