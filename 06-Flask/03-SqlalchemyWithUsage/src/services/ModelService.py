from src.core.metaclass.Singleton import Singleton


class ModelService(metaclass=Singleton):
    models = None
    schemas = None

    def initialize(self):
        from src.models import metadata
        self.models = metadata.get("models")
        self.schemas = metadata.get("schemas")

        return ModelService()

    def getModel(self, model_name):
        model = self.models.get(model_name)

        if model is not None:
            return self.models.get(model_name)
        else:
            print("Model Yok!")

    def getSchema(self, schema_name):
        schema = self.schemas.get(schema_name)

        if schema is not None:
            return self.schemas.get(schema_name)
        else:
            print("Schema Yok!")


def serve_model() -> ModelService:
    return ModelService()
