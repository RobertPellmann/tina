class TinaBootstrapper:
    def __init__(self, app,  registry):
        routes = registry.routes
        routes.register(app)