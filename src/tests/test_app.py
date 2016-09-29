# -*- coding: utf-8 -*-
from unittest import mock
import toolz


from app.facebook.utils import create_template


async def test_index(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world' in text


async def test_facebook_verification_success(cli, app):
    subscribe_challenge = 'qwerty'
    resp = await cli.get(
        '/api/facebook/?hub.challenge={challenge}&'
        'hub.mode=subscribe&hub.verify_token={token}'.format(
            token=app['config'].facebook_verification_token,
            challenge=subscribe_challenge
        )
    )
    assert resp.status == 200
    text = await resp.text()
    assert text == subscribe_challenge


async def test_facebook_verification(cli, app):
    subscribe_challenge = 'qwerty'
    resp = await cli.get(
        '/api/facebook/?hub.challenge={challenge}&'
        'hub.mode=subscribe&hub.verify_token={token}'.format(
            token='fake_token',
            challenge=subscribe_challenge
        )
    )
    assert resp.status == 403
    text = await resp.text()
    assert text == ''


async def test_facebook_message_hook(cli, app, get_json_resurce):
    token = 'facebook_access_token'
    _, data = get_json_resurce('fb_message.json')

    sended_messages = []
    used_tokens = set()
    async def mocked(message, token, *args):
        used_tokens.add(token)
        sended_messages.append(message)

    with mock.patch('app.facebook.api.call_messages_api', new=mocked):
        resp = await cli.post(
            '/api/facebook/',
            headers={'Content-Type': 'application/json'},
            data=data
        )
    assert resp.status == 200
    assert used_tokens == {token}
    assert set(toolz.map(
        lambda m: (toolz.get_in(['recipient', 'id'], m),
                   toolz.get_in(['message', 'text'], m)),
        sended_messages
    )) == {('1225682400836903', 'hello'), ('1225682400836902', 'hello2')}


def test_create_template():
    template = create_template('greeting')
    assert template.__name__ == 'greeting'
    assert template() in """
{
  "setting_type":"greeting",
  "greeting":{
    "text":"Hi {{user_first_name}}, welcome to this Sample bot"
  }
}
    """

def test_create_template_loads():
    template = create_template('greeting', loads=True)
    assert template.__name__ == 'greeting'
    assert template() == {
        'greeting': {'text': 'Hi {{user_first_name}}, welcome to this Sample bot'},
        'setting_type': 'greeting'
    }
