'''
WSGI Settings for Project

by podobongbong (podobong00@gmail.com)
'''

import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

application = get_wsgi_application()
