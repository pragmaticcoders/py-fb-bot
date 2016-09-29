# -*- coding: utf-8 -*-

from aiohttp import web, ClientSession

from .routes import setup as setup_routers
from .facebook.api import register_greeting


CLIENT_SESSION_KEY = 'client_session'


async def on_startup(app):
    client_session = ClientSession(loop=app.loop)
    await client_session.__aenter__()
    app[CLIENT_SESSION_KEY] = client_session
    config = app['config']
    if not config.test:
        await register_greeting(
            config.facebook_page_id,
            config.facebook_access_token,
            client_session
        )


async def on_shutdown(app):
    client_session = app.get(CLIENT_SESSION_KEY)
    if client_session is not None:
        await client_session.close()


def create(loop, conf=None):
    if conf is None:
        from .config import Main
        conf = Main

    app = web.Application(loop=loop)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    app[CLIENT_SESSION_KEY] = ClientSession(loop=loop)

    conf.setup(app)
    setup_routers(app)

    return app
