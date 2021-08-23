class Service:
    def __init__(self):
        from manage import ModelModule, db
        self.ModelModule = ModelModule
        self.db = db

    def getModels(self, model_list):
        models = []
        for model in model_list:
            models.append(self.ModelModule.getModel(model))

        return tuple(models)

    def getSchemas(self, schema_list):
        schemas = []
        for schema in schema_list:
            schemas.append(self.ModelModule.getSchema(schema))

        return tuple(schemas)
