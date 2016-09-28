# -*- coding: utf-8 -*-
import asyncio
import json
import logging

import aiohttp
import toolz

logger = logging.getLogger(__name__)


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
        logger.warning(await resp.text())


async def send_text_message(text, recipend_id, token, client_session):
    await call_messages_api({
        'recipient': {'id': recipend_id},
        'message': {'text': text}
    }, token, client_session)


def echo(data, token, client_session, loop, send_coroutine=None):
    if send_coroutine is None:
        send_coroutine = send_text_message
    if not is_page_event(data):
        return
    echo_mssages = []
    for item in data.get('entry', []):
        for message in item.get('messaging', []):
            echo_mssages.append(send_coroutine(
                toolz.get_in(['message', 'text'], message),
                toolz.get_in(['sender', 'id'], message),
                token,
                client_session
            ))
    return asyncio.gather(*echo_mssages, loop=loop)
