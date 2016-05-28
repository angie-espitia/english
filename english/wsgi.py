
import os

from django.core.wsgi import get_wsgi_application
'''
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "english.settings")

application = get_wsgi_application()


#!/usr/bin/python
import os, sys

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))
os.environ['DJANGO_SETTINGS_MODULE'] = 'english.settings'

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'

os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.7/site-packages')

virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()'''

#!/usr/bin/python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "english.settings")
from django.core.wsgi import get_wsgi_application
from dj_static import Cling
application = Cling(get_wsgi_application())