#! /usr/bin/env python

import sys
import logging


logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/dgrajo/Python/Projects/py361/nkp')


from nkp import app as application
application.secret_key = 'this%is&my^key$you'
