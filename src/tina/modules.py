from flask import request
from .route import GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE, PATCH, Routes
from .response import NotAllowed
from .diagnostics import debug

class TinaModuleRegistry:
    def __init__(self):
        self.routes = Routes()
        self.modules = []
    def add(self, tina_module_class):
        if issubclass(tina_module_class, TinaModule):
            tina_module_class(self.routes)
            self.modules.append(tina_module_class)
            debug('Module ' + str(tina_module_class) + ' registered')
        else:
            debug('The class ' + str(tina_module_class) + ' is not a tina module')

module_registry = TinaModuleRegistry()

class TinaModule:
    def __init__(self, routes):
        self.routes = routes
        self.register_routes()
    def register_routes(self):
        pass
    def get(self, path, handler, **kwargs):
        self.routes.add(GET, path, handler, **kwargs)
    def head(self, path, handler, **kwargs):
        self.routes.add(HEAD, path, handler, **kwargs)
    def post(self, path, handler, **kwargs):
        self.routes.add(POST, path, handler, **kwargs)
    def put(self, path, handler, **kwargs):
        self.routes.add(PUT, path, handler, **kwargs)
    def delete(self, path, handler, **kwargs):
        self.routes.add(DELETE, path, handler, **kwargs)
    def connect(self, path, handler, **kwargs):
        self.routes.add(CONNECT, path, handler, **kwargs)
    def options(self, path, handler, **kwargs):
        self.routes.add(OPTIONS, path, handler, **kwargs)
    def trace(self, path, handler, **kwargs):
        self.routes.add(TRACE, path, handler, **kwargs)
    def patch(self, path, handler, **kwargs):
        self.routes.add(PATCH, path, handler, **kwargs)
