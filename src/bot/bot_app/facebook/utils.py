# -*- coding: utf-8 -*-

import os
import json
from  string import Template


ROOT = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_ROOT = os.path.join(ROOT, 'templates')


def create_template(name, path=None, loads=False):
    if path is None:
        path = '.'.join([name, 'json'])
    path_abs = os.path.join(TEMPLATES_ROOT, path)

    with open(path_abs) as fp:
        template = Template(fp.read())

    def to_string(*args, **kwargs):
        text = template.substitute(*args, **kwargs)
        if loads:
            return json.loads(text)
        return text
    to_string.__name__ = name

    return to_string
