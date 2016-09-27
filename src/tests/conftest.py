# -*- coding: utf-8 -*-

import os
import sys


import pytest
from aiohttp import web

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
SRC_ROOT = os.path.dirname(TESTS_ROOT)

sys.path.append(SRC_ROOT)


@pytest.fixture()
def app(loop):
    from app import create
    return create(loop=loop)


@pytest.fixture()
def cli(test_client, app, loop):
    return loop.run_until_complete(test_client(app))
