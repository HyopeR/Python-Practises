from flask_migrate import Migrate
from src.core.metaclass.Singleton import Singleton


class MigrationService(metaclass=Singleton):
    migrate: Migrate = None

    def initialize(self, app, db):
        self.migrate = Migrate(app, db)

        # TODO: Dont delete this. Migration import models.
        from src.models import metadata

        return MigrationService()


def serve_migrate() -> MigrationService:
    return MigrationService()
