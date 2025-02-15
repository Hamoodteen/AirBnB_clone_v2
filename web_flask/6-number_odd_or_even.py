#!/usr/bin/python3
"""commenttttttttttttttttttttttttttttttttttttt"""
from flask import Flask, render_template
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
@app.route('/c/', strict_slashes=False)
def c_text(text="is_cool"):
    """commenttttttttttttttttttttttttttttttttttttt"""
    formatted = text.replace('_', ' ')
    return f'C {formatted}'


@app.route('/python/(<text>)', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def py_text(text="is_cool"):
    """commenttttttttttttttttttttttttttttttttttttt"""
    formatted = text.replace('_', ' ')
    return f'Python {formatted}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """commenttttttttttttttttttttttttttttttttttttt"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """commenttttttttttttttttttttttttttttttttttttt"""
    return render_template('5-number.html', intnumber=f'Number: {n}')


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_oddeven(n):
    """commenttttttttttttttttttttttttttttttttttttt"""
    file = '6-number_odd_or_even.html'
    if n % 2 == 0:
        return render_template(file, oddeven=f'Number: {n} is even')
    return render_template(file, oddeven=f'Number: {n} is odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
