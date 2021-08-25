from flask_marshmallow import Marshmallow
from src import app
from src.services.EnvironmentService import EnvironmentService
from src.services.AlchemyService import AlchemyService
from src.services.MigrationService import MigrationService
from src.services.ModelService import ModelService

EnvModule = EnvironmentService().initialize(app)
AlchemyModule = AlchemyService().initialize(app)
db = AlchemyModule.db
ma = Marshmallow(app)

MigrationModule = MigrationService().initialize(app, db)
ModelModule = ModelService().initialize()
