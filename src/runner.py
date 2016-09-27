#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import asyncio

from aiohttp import web

SRC_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(SRC_ROOT)


from app import create as create_app
loop = asyncio.get_event_loop()

app = create_app(loop=loop)


def main():
    from aiohttp_utils import run
    web.run_app(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':
    main()
