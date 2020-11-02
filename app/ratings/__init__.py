# app/ratings/__init__.py

from flask import Blueprint

ratings = Blueprint('ratings', __name__)

from . import views  # noqa
