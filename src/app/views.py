# -*- coding: utf-8 -*-

import logging

from aiohttp import web
from aiohttp.web import Response
from schema import SchemaError

from .facebook.api import is_valid_subscribe
from .facebook.bot import  echo
from .schema.facebook import fb_message

logger = logging.getLogger(__name__)


class Index(web.View):
    async def get(self):
        return Response(text='Hello, world')


class Facebook(web.View):

    @property
    def facebook_verification_token(self):
        return self.request.app['config'].facebook_verification_token

    @property
    def facebook_access_token(self):
        return self.request.app['config'].facebook_access_token

    async def get(self):
        data = self.request.GET
        token = self.facebook_verification_token
        if is_valid_subscribe(data, token):
            response = web.Response(text=data.get('hub.challenge'))
        else:
            response = web.Response()
            response.set_status(403)
        return response

    async def post(self):
        text = await self.request.text()
        client_session = self.request.app['client_session']
        token = self.facebook_access_token
        loop = self.request.app.loop

        try:
            data = fb_message.validate(text)
            await echo(data, token, client_session, loop)
        except SchemaError as error:
            logger.exception(error)

        return web.Response()
