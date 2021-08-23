from src.models.TaskCategory import TaskCategory
from src.models.Task import Task
from src.models.Category import Category

from src.models.schemas.Task import task_schema, tasks_schema

metadata = {
    "models": {
        "TaskCategory": TaskCategory,
        "Task": Task,
        "Category": Category
    },

    "schemas": {
        "Task": task_schema,
        "Tasks": tasks_schema
    }
}
