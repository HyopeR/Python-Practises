from src.services.MigrationService import MigrationService
from src import app
from src import db

migration_service = MigrationService().initialize(app, db)
