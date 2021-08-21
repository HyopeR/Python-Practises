from src.core.metaclass.Singleton import Singleton


class ModelService(metaclass=Singleton):
    metadata = None

    def initialize(self):
        from src.models import metadata
        self.metadata = metadata

        return ModelService()

    def getModel(self, model_name):
        model = self.metadata.get(model_name)

        if model is not None:
            return self.metadata.get(model_name)
        else:
            print("Model Yok!")


def serve_model() -> ModelService:
    return ModelService()
