from src.models.TaskCategory import TaskCategory
from src.models.Task import Task
from src.models.Category import Category
from src.models.User import User

from src.models.schemas.Task import task_schema, tasks_schema
from src.models.schemas.Category import category_schema, categories_schema
from src.models.schemas.User import user_schema

metadata = {
    "models": {
        "TaskCategory": TaskCategory,
        "Task": Task,
        "Category": Category,
        "User": User,
    },

    "schemas": {
        "Task": task_schema,
        "Tasks": tasks_schema,
        "Category": category_schema,
        "Categories": categories_schema,
        "User": user_schema,
    }
}
