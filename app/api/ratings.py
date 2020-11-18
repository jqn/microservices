from . import api
import json
import os
import sys
from flask import request, jsonify
import MySQLdb
import itertools
import pprint
import json
from .. import db


@api.route('v1.0/ratings', methods=['GET', 'POST'])
def get_ratings():
    condition = request.form['condition']
    year = request.form['year']
    make = request.form['make']
    model = request.form['model']
    rating = dealRating()

    ratings = rating.get_vehicles(
        rating.db_connection(), condition, year, make, model)

    print("ratings")
    pprint.pprint(ratings)

    return json.dumps(ratings)


@api.route('v1.0/ratings/years', methods=['GET', 'POST'])
def get_years():
    condition_val = request.form['condition']

    query = db.session.execute(
        "SELECT DISTINCT year FROM vehicle_vehicle WHERE new_used= :val ORDER BY year DESC", {'val': condition_val})

    # Use list comprehension to format the query result
    # from a list of tuples to a list of strings
    result = [r for (r,) in query]

    return jsonify({'years': result})


@api.route('v1.0/ratings/makes', methods=['GET', 'POST'])
def get_makes():
    vehicle_condition = request.form['condition']
    vehicle_year = request.form['year']

    query = db.session.execute("SELECT DISTINCT make FROM vehicle_vehicle WHERE new_used= :condition AND year= :year", {
                               'condition': vehicle_condition, 'year': vehicle_year})

    # Use list comprehension to format the query result
    # from a list of tuples to a list of strings
    result = [r for (r,) in query]

    return jsonify({'makes': result})


@api.route('v1.0/ratings/models', methods=['GET', 'POST'])
def get_models():
    vehicle_condition = request.form['condition']
    vehicle_year = request.form['year']
    vehicle_make = request.form['make']

    query = db.session.execute("SELECT DISTINCT model FROM vehicle_vehicle WHERE new_used= :condition AND year= :year AND make= :make", {
                               'condition': vehicle_condition, 'year': vehicle_year, 'make': vehicle_make})

    # Use list comprehension to format the query result
    # from a list of tuples to a list of strings
    result = [r for (r,) in query]

    return jsonify({'models': result})


class dealRating():
    """ Deal Rating class for generating
    a deal rating system from T1 and T2 vehicles

    Attributes:

    """

    def __init__(self):
        pass

    def get_vehicles(self, db, condition, year, make, model):
        """Method to query all vehicle from the vehicle table.

        Args:
            condition (string): vehicle new/used category
            year (string): vehicle year
            make (string): vehicle make
            model (string): vehicle model

        Returns:
            dictionary: vehicle data set

        """

        # The default cursor class except it returns rows as dictionaries.
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        # A “server-side” cursor. It uses CursorUseResultMixIn. Use only if you are dealing with potentially large result sets.
        # returns rows as dictionaries
        # cursor = db.cursor.cursors.SSDictCursor)

        print(condition)
        print(year)
        print(make)
        print(model)

        cursor.execute(
            """SELECT id, year, make, model, series, mileage FROM vehicle_vehicle WHERE new_used=%s
            AND year=%s AND make=%s AND model=%s AND data_tier<=2 AND mileage BETWEEN 1000 AND 10000 ORDER BY series ASC""", (condition, year, make, model))

        result = cursor.fetchall()
        cursor.close()

        groups = self.group_by_trim(result)
        # pprint.pprint(groups)

        response = self.rate(groups)

        return response

    def group_by_trim(self, results):
        # Combine vehicles into groups by trim(unique trims)
        groups = []
        uniquekeys = []

        for k, g in itertools.groupby(results,  key=lambda x: x['series']):
            groups.append(list(g))      # Store group iterator as a list
            uniquekeys.append(k)

        trims_group = dict(zip(uniquekeys, groups))

        return trims_group

    def rate(self, groups):
        # Split each trim group into mileage groups like this
        # incredible (lowest 25%)
        # great_price (25%)
        # good_price (25%)
        # fair_price (25%)
        # unknown
        incredible = []
        great_price = []
        good_price = []
        fair_price = []
        unknown = []

        # pprint.pprint(groups)

        for key in groups:
            incredible.extend(
                [d for d in groups.get(key) if d['mileage'] in range(6, 2501)])
            great_price.extend(
                [d for d in groups.get(key) if d['mileage'] in range(2501, 5001)])
            good_price.extend(
                [d for d in groups.get(key) if d['mileage'] in range(5001, 7501)])
            fair_price.extend(
                [d for d in groups.get(key) if d['mileage'] in range(7501, 10001)])
            unknown.extend(
                [d for d in groups.get(key) if d['mileage'] >= 10001])

        results = json.dumps({'incredible': incredible,
                              'great_price': great_price, 'good_price': good_price, 'fair_price': fair_price, 'unknown': unknown})

        # print(results)

        return results

    def db_connection(self):
        """Method to create a database connection.

        Args:
            None

        Returns:
            object: the database connection object

        """
        print(os.environ['DB_NAME'])
        return MySQLdb.connect(os.environ['DB_HOSTNAME'], os.environ['DB_USERNAME'], os.environ['DB_PASSWORD'], os.environ['DB_NAME'])
