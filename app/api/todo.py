from . import api
from flask import request
from flask_login import current_user
import json

from app.models import Todo


@api.route('/todo/add', methods=['POST'])
def add_todo():
    # load JSON data from request
    data = json.loads(request.data)
    print(data)
    Todo(data["title"], data["description"],
         created_by=current_user.email).save()
    return json.dumps(data)


@api.route('/todo/delete/<int:id>', methods=['POST'])
def delete_todo(id):
    # load JSON data from request
    data = json.loads(request.data)
    return json.dumps(data)


@api.route('/todo/update/<int:id>', methods=['POST'])
def update_todo(id):
    Todo.query.filter_by(id=int(id)).delete()
    return json.dumps({'message': 'Todo removed successfully'})


@api.route('/todo/all', methods=['GET'])
def get_todos():
    context = dict()
    context['todos'] = current_user.todos
    context['items_left'] = len(
        [todo for todo in current_user.todos if not todo.is_completed])
    return json.dumps(context)
