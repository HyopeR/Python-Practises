from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.core.decorators.interceptor import interceptor
from src.routes.task.task_dto import TaskPostDto, TaskPutDto
from src.routes.task.task_controller import TaskController

task_route = Blueprint('task', __name__, template_folder='../../templates')


@task_route.route("/task", methods=['GET'])
@interceptor
def get():
    TaskController().get()
    return {}


@task_route.route("/task/<id>", methods=['GET'])
def get_one(id):
    return TaskController().post(id)


@task_route.route("/task", methods=['POST'])
@validate_json
@validate_schema(schema=TaskPostDto())
def post():
    body = request.get_json()
    return TaskController().post(body)


@task_route.route("/task/<id>", methods=['PUT'])
@validate_json
@validate_schema(schema=TaskPutDto())
def put(id, body):
    body = request.get_json()
    return TaskController().put(body)


@task_route.route("/task/<id>", methods=['DELETE'])
def delete(id):
    return TaskController().delete(id)
