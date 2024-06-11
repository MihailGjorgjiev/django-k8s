"""
WSGI config for django_k8s project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import pathlib
import dotenv
from django.core.wsgi import get_wsgi_application

CURR_DIR = pathlib.Path(__file__).resolve().parent
BASE_DIR = CURR_DIR.parent
ENV_FILE_DIR = BASE_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_k8s.settings')

application = get_wsgi_application()
