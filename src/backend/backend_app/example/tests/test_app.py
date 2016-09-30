# -*- coding: utf-8 -*-


def test_with_client(client):
    response = client.get('/')
    assert '<h1>Not Found</h1>' in str(response.content)
