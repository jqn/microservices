from . import api
from flask import request
import json


@api.route('/todo/add', methods=['POST'])
def add_todo():
    # load JSON data from request
    data = json.loads(request.data)
    return json.dumps(data)


@api.route('/todo/delete', methods=['POST'])
def delete_todo():
    # load JSON data from request
    data = json.loads(request.data)
    return json.dumps(data)


@api.route('/todo/update', methods=['POST'])
def update_todo():
    # load JSON data from request
    data = json.loads(request.data)
    return json.dumps(data)


@api.route('/todo/all', methods=['GET'])
def get_todos():
    # load JSON data from request
    data = json.loads(request.data)
    return json.dumps(data)
