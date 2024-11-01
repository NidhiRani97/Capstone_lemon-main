"""
ASGI configuration for the Little Lemon project.

This file exposes the ASGI callable as a module-level variable named `application`.

For more details, refer to:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Set the default settings module for the Django ASGI application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "littlelemon.settings")

# Create the ASGI application callable
application = get_asgi_application()
