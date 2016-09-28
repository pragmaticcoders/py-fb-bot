# -*- coding: utf-8 -*-
from os import environ as env


class Base:

    @classmethod
    def setup(cls, app):
        app['config'] = cls


class Main(Base):
    facebook_access_token = env.get(
        'FACEBOOK_ACCESS_TOKEN',
        'facebook_access_token'
    )
    facebook_verification_token = env.get(
        'FACEBOOK_VERIFICATION_TOKEN',
        'facebook_verification_token'
    )


class Test(Main):
    test = True
