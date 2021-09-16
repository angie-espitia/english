# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "english.settings")

# application = get_wsgi_application()



#!/usr/bin/python

import os

from django.core.wsgi import get_wsgi_application
# from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'english.settings')

application = get_wsgi_application()

# application = Cling(get_wsgi_application())
