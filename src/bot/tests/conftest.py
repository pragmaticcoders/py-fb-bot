# -*- coding: utf-8 -*-

import os
import sys
import json

import pytest
from aiohttp import web

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_ROOT = os.path.dirname(TESTS_ROOT)

sys.path.append(SRC_ROOT)
print(sys.path)


@pytest.fixture()
def app(loop):
    from bot_app import create
    from bot_app.config import Test
    _app = create(loop=loop, conf=Test)
    loop.run_until_complete(_app.startup())
    return _app


@pytest.fixture()
def cli(test_client, app, loop):
    return loop.run_until_complete(test_client(app))


@pytest.fixture()
def get_resurce_path():
    return lambda p: os.path.join(TESTS_ROOT, 'resurces', p)


@pytest.fixture()
def get_json_resurce(get_resurce_path):
    def getter(path):
        with open(get_resurce_path(path)) as fp:
            data = fp.read()
            return json.loads(data), data
    return getter
