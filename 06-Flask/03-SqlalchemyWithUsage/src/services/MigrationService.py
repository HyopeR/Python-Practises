from flask_migrate import Migrate
from src.core.metaclass.Singleton import Singleton


class MigrationService(metaclass=Singleton):
    migrate: Migrate = None

    def initialize(self, app, db):
        self.migrate = Migrate(app, db)
        from src.models.index import metadata

        return MigrationService()
