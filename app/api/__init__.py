# app/admin/__init__.py
from flask import Blueprint

api = Blueprint('api', __name__)

from . import users, errors, tokens, todo  # noqa
