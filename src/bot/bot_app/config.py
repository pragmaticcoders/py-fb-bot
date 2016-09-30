# -*- coding: utf-8 -*-
from os import environ as env


class Base:

    @classmethod
    def setup(cls, app):
        app['config'] = cls


class Main(Base):
    test = False
    facebook_access_token = env.get(
        'FACEBOOK_ACCESS_TOKEN',
        'facebook_access_token'
    )
    facebook_verification_token = env.get(
        'FACEBOOK_VERIFICATION_TOKEN',
        'facebook_verification_token'
    )
    facebook_page_id = env.get(
        'FACEBOOK_PAGE_ID',
        'facebook_page_id'
    )


class Test(Main):
    test = True
