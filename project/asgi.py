import os

from django.core.asgi import get_asgi_application
from project.settings.base import env

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))

application = get_asgi_application()
