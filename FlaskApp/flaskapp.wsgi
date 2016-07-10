#!/usr/bin/python
import sys
import logging
logging.basicConfig( stream = sys . stderr )
sys.path.insert ( 0 , "/var/test_server/FlaskApp/" )
from DowningJones import app as application
application.secret_key = 'my secret key.'
