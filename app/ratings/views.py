# app/ratings/views.py

from flask import render_template

from . import ratings
from .. import db
from ..models import VehicleVehicle


@ratings.route('/ratings')
def ratings():
    """
    Render the ratings template on the /ratings route
    """
    makes = db.session.execute(
        "SELECT DISTINCT make FROM vehicle_vehicle")

    models = db.session.execute(
        "SELECT DISTINCT model FROM vehicle_vehicle")

    years = db.session.execute(
        "SELECT DISTINCT year FROM vehicle_vehicle")
    # for make in makes:
    # print(make[0])
    # print(make[0])  # Access by positional index
    # print(make['make'])  # Access by column name as a string
    # r_dict = dict(make.items())  # convert to dict keyed by column names
    # print(r_dict)

    return render_template('ratings/ratings.html', title="Deal Ratings", makes=makes, models=models, years=years,)
