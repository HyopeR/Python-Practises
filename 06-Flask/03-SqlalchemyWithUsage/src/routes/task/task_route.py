from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.core.decorators.interceptor import interceptor
from src.routes.task.task_dto import TaskPostDto, TaskPutDto
from src.routes.task.task_controller import TaskController
from collections import namedtuple

task_route = Blueprint('task', __name__, template_folder='../../templates')


@task_route.route("/task", methods=['GET'])
@interceptor
def get():
    return TaskController().get()


@task_route.route("/task/<id>", methods=['GET'])
@interceptor
def get_one(id):
    return TaskController().get_one(id)


@task_route.route("/task", methods=['POST'])
@validate_json
@validate_schema(schema=TaskPostDto())
@interceptor
def post():
    body = request.get_json()
    body_tuple = namedtuple('body', body.keys())(*body.values())
    return TaskController().post(body_tuple)


@task_route.route("/task/<id>", methods=['PUT'])
@validate_json
@validate_schema(schema=TaskPutDto())
@interceptor
def put(id):
    body = request.get_json()
    body_tuple = namedtuple('body', body.keys())(*body.values())
    return TaskController().put(id, body_tuple)


@task_route.route("/task/<id>", methods=['DELETE'])
@interceptor
def delete(id):
    return TaskController().delete(id)
