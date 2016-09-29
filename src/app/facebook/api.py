# -*- coding: utf-8 -*-
import json
import logging

import aiohttp

from .utils import create_template


logger = logging.getLogger(__name__)


greeting_template = create_template('greeting')


def is_valid_subscribe(data, token):
    return (data.get('hub.mode') == 'subscribe' and
            data.get('hub.verify_token') == token)


def is_page_event(data):
    return data.get('object') == 'page'


async def call_messages_api(message, token, client_session):
    kwargs = {
        'headers': {'Content-Type': 'application/json'},
        'data': json.dumps(message),
        'params': {'access_token': token}
    }
    async with client_session.post(
            'https://graph.facebook.com/v2.6/me/messages',
            **kwargs
    ) as resp:
        if resp.status_code != 200:
            logger.warning(await resp.text())


async def send_text_message(text, recipend_id, token, client_session):
    await call_messages_api({
        'recipient': {'id': recipend_id},
        'message': {'text': text}
    }, token, client_session)
