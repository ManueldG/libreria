activate_this = 'C:/Users/myuser/Envs/my_application/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/myuser/Envs/my_application/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/myuser/my_application')
sys.path.append('C:/Users/myuser/my_application/my_application')

os.environ['DJANGO_SETTINGS_MODULE'] = 'my_application.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_application.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()