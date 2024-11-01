"""
WSGI configuration for the Little Lemon project.

This file exposes the WSGI callable as a module-level variable named `application`.

For more details, visit:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")

# Create the WSGI application callable
application = get_wsgi_application()
