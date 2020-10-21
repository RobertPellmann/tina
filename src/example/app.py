import os
from flask import Flask, Response
from tina import TinaBootstrapper
from tina.modules import TinaModule, module_registry

app = Flask(__name__)

def tina_module(self):
    module_registry.add(self)

@tina_module
class HelloWorldModule(TinaModule):
    def register_routes(self):
        self.get('/', self.get_hello_world)
    def get_hello_world(*args):
        return 'Hello World'

bootstrapper = TinaBootstrapper(app, module_registry)