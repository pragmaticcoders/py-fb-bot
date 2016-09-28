# -*- coding: utf-8 -*-
"""setup python path"""

import os
import sys


SRC_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(SRC_ROOT)

from app import create
