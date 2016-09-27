# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp.web import Response


async def index(request):
    return Response(text='Hello, world')


def create(loop):
    app = web.Application(loop=loop)
    app.router.add_get('/', index)
    return app
