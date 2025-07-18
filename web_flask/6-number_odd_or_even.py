#!/usr/bin/python3

"""Script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(_name_)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Comment"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Comment"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text_route(text):
    """Comment"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def text_route_python(text="is cool"):
    """Comment"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    """Comment"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_route_template(n):
    """Comment"""
    return render_template("5-number.html", num=n)


@app.route('/number_odd_or_even/<int:n>')
def num_odd_or_even(n):
    """Comment"""
    even_or_odd = "even" if n%2 == 0 else "odd"
    values = {
        "num": n,
	"even_or_odd": even_or_odd
    }
    return render_template('6-number_odd_or_even.html', values=values)


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
