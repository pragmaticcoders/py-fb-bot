import re

class PrefixMiddleware:

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix
        self.re = re.compile('^%s(.*)$' % (self.prefix, ))

    def __call__(self, environ, start_response):
        url = environ['PATH_INFO']
        url = re.sub(self.re, r'\1', url) or '/'
        environ['PATH_INFO'] = url
        environ['SCRIPT_NAME'] = self.prefix
        return self.app(environ, start_response)
