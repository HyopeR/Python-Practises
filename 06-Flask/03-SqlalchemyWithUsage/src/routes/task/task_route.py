from flask import Blueprint, request
from src.core.decorators.validate_json import validate_json
from src.core.decorators.validate_schema import validate_schema
from src.routes.task.task_dto import TaskPostDto, TaskPutDto
from src.routes.task.task_controller import TaskController

task_route = Blueprint('task', __name__, template_folder='../../templates')


@task_route.route("/task", methods=['GET'])
def get():
    return TaskController().get()


# @task_route.route("/task/<id>", methods=['GET'])
# def get_one(id):
#     return TaskController().post(id)
#
#
# @task_route.route("/task", methods=['POST'])
# @validate_json
# @validate_schema(schema=TaskPostDto())
# def post():
#     body = request.get_json()
#     return TaskController().post(body)
#
#
# @task_route.route("/task/<id>", methods=['PUT'])
# @validate_json
# @validate_schema(schema=TaskPutDto())
# def post(id, body):
#     body = request.get_json()
#     return TaskController().put(body)
#
#
# @task_route.route("/task/<id>", methods=['DELETE'])
# def post(id):
#     return TaskController().delete(id)
