# -*- coding: utf-8 -*-


async def test_hello(cli):
    resp = await cli.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world' in text
