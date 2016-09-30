# -*- coding: utf-8 -*-
import asyncio

import toolz

from .api import send_text_message, is_page_event


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
