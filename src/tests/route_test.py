import pytest
from flask import Response
from tina.route import Route, GET, POST

default_path = '/'
default_handler = lambda context: Response() 

def test_method_gets_added():
    # arrange
    method = GET
    handler = default_handler
    route = Route(default_path)
    route.add_handler(method, handler)
    # act
    methods = route.methods()
    # assert
    assert len(methods) == 1
    assert methods[0] == GET

def test_multiple_methods():
    # arrange
    route = Route(default_path)
    route.add_handler(GET, default_handler)
    route.add_handler(POST, default_handler)
    # act
    methods = route.methods()
    # assert
    assert len(methods) == 2
    assert GET in methods
    assert POST in methods

def test_adding_same_method_twice():
    # arrange
    route = Route(default_path)
    route.add_handler(GET, default_handler)
    route.add_handler(GET, default_handler)
    # act
    methods = route.methods()
    assert len(methods) == 1
    assert methods[0] == GET