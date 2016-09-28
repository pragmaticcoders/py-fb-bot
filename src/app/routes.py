# -*- coding: utf-8 -*-
from .views import Index, Facebook


ROUTERS = (
    ('/', Index, 'index'),
    ('/api/facebook/', Facebook, 'facebook')
)


def setup(app):
    for path, handler, name in ROUTERS:
        resource = app.router.add_resource(path, name=name)
        route = resource.add_route('*', handler)
