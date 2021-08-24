from manage import db
from sqlalchemy.dialects.postgresql import INTEGER

TaskUser = db.Table(
    'task_user',
    db.Column('task_id', INTEGER, db.ForeignKey('task.id')),
    db.Column('user_id', INTEGER, db.ForeignKey('user.id')),
)