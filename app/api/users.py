from . import api
import json


@api.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass


@api.route('/users', methods=['POST'])
def get_users():
    return json.dumps({'status': 'OK', 'user': '', })
