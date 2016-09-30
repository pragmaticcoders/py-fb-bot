# -*- coding: utf-8 -*-
import json
import logging

import aiohttp

from .utils import create_template


logger = logging.getLogger(__name__)


greeting_template = create_template('greeting')
message_template = create_template('message')


def is_valid_subscribe(data, token):
    return (data.get('hub.mode') == 'subscribe' and
            data.get('hub.verify_token') == token)


def is_page_event(data):
    return data.get('object') == 'page'


async def call_api(url, template, token, client_session, context={}):
    kwargs = {
        'headers': {'Content-Type': 'application/json'},
        'data': template(**context),
        'params': {'access_token': token}
    }
    async with client_session.post(url, **kwargs) as resp:
        if resp.status != 200:
            logger.warning(await resp.text())

async def call_thread_settings(template, page_id, token, client_session,
                               context={}):
    url = 'https://graph.facebook.com/v2.6/{page_id}/thread_settings'.format(
        page_id=page_id,
    )
    await call_api(url, template, token, client_session, context)


async def call_messages_api(template, token, client_session, context={}):
    url = 'https://graph.facebook.com/v2.6/me/messages'
    await call_api(url, template, token, client_session, context)


async def send_text_message(text, recipient_id, token, client_session):
    context = {
        'recipient_id': recipient_id,
        'text': text
    }
    await call_messages_api(
        message_template, token, client_session, context=context
    )


async def register_greeting(page_id, token, client_session):
    await call_thread_settings(
        greeting_template,  page_id, token, client_session
    )
