from .base import *
import os

DEBUG = bool(os.environ.get('DJANGO_DEBUG', 0))

ALLOWED_HOSTS = [] if DEBUG else os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')