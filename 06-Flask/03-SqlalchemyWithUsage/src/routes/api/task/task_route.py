from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.utils.decorators.interceptor import interceptor
from src.routes.api.task.task_dto import TaskPostDto, TaskPutDto
from src.routes.api.task.task_controller import TaskController

task_route = Blueprint('task', __name__, template_folder='../../templates')


@task_route.route("/task", methods=['GET'])
@interceptor
def get():
    return TaskController().get()


@task_route.route("/task/<int:id>", methods=['GET'])
@interceptor
def get_one(id):
    return TaskController().get_one(id)


@task_route.route("/task", methods=['POST'])
@validate_json
@validate_schema(schema=TaskPostDto())
@interceptor
def post():
    body: dict = request.get_json()
    return TaskController().post(body)


@task_route.route("/task/<int:id>", methods=['PUT'])
@validate_json
@validate_schema(schema=TaskPutDto())
@interceptor
def put(id):
    body: dict = request.get_json()
    return TaskController().put(id, body)


@task_route.route("/task/<int:id>", methods=['DELETE'])
@interceptor
def delete(id):
    return TaskController().delete(id)
