#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio

from aiohttp import web

from .wrapper import create as create_app
loop = asyncio.get_event_loop()

app = create_app(loop=loop)


def main():
    from aiohttp_utils import run
    web.run_app(app, host='0.0.0.0', port='8080')


if __name__ == '__main__':
    main()
