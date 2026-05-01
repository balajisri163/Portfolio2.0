"""
WSGI config for personal_website project.
"""

import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_website.settings')

BASE_DIR = Path(__file__).resolve().parent.parent

application = get_wsgi_application()
application = WhiteNoise(application)
application.add_files(BASE_DIR / 'media', prefix='media/')