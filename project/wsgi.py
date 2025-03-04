import os

from django.core.wsgi import get_wsgi_application
from project.settings.base import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()
