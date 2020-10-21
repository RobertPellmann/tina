from flask import request
from collections.abc import Callable
from tina.context import TinaContext
from tina.response import NotAllowed

GET = 'GET'
HEAD = 'HEAD'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'
CONNECT = 'CONNECT'
OPTIONS = 'OPTIONS'
TRACE = 'TRACE'
PATCH = 'PATCH'

METHODS = [GET, HEAD, POST, PUT, DELETE, OPTIONS, TRACE, PATCH]

class Routes:
    def __init__(self):
        self.routes = {}
    def add(self, method, path, handler, **kwargs):
        if path not in self.routes:
            self.routes[path] = Route(path)
        self.routes[path].add_handler(method, handler, **kwargs)
    def register(self, app):
        for path in self.routes:
            route = self.routes[path]
            @app.route(route.path, methods = route.methods())
            def flask_route(*args):
                return route.dispatch(request)

class Handler:
    def __init__(self, process, **kwargs):
        self.process = process
        self.condition = kwargs.get('condition', False)
    def __call__(self, *args):
        return self.process(*args)

class Route:
    def __init__(self, path):
        self.path = path
        self.handlers = {}
    def add_handler(self, method, handler, **kwargs):
        if method not in self.handlers:
            self.handlers[method] = []
        self.handlers[method].append(Handler(handler, **kwargs))
    def methods(self):
        return [method for method in self.handlers]

    def dispatch(self, request, *args):
        context = TinaContext(request)
        method_handlers = self.handlers.get(request.method)
        for handler in [handler for handler in method_handlers if handler.condition]:
            if handler.condition(context):
                handler(*args)
        for handler in [handler for handler in method_handlers if not handler.condition]:
            return handler(*args)
        return NotAllowed()