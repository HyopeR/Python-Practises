from src import app
from src.services.EnvironmentService import EnvironmentService
from src.services.AlchemyService import AlchemyService
from src.services.MigrationService import MigrationService
from src.services.ModelService import ModelService
from src.services.ErrorService import ErrorService

EnvModule = EnvironmentService().initialize(app)
AlchemyModule = AlchemyService().initialize(app)
db = AlchemyModule.db

MigrationModule = MigrationService().initialize(app, db)
ModelModule = ModelService().initialize()
ErrorModule = ErrorService().initialize()
