#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy Session.
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display a HTML page like 8-index.html
    """
    states = storage.all(State)
    cities = storage.all(City)
    amenities = storage.all(Amenity)
    places = storage.all(Place)

    return render_template('100-hbnb.html',
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', 5000)
    app.run(host=host, port=port)
