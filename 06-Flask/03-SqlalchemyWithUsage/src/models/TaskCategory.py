from manage import db
from sqlalchemy.dialects.postgresql import INTEGER

TaskCategory = db.Table(
    'task_category',
    db.Column('task_id', INTEGER, db.ForeignKey('task.id')),
    db.Column('category_id', INTEGER, db.ForeignKey('category.id')),
)