from .base import *
from .base import env

DEBUG = True

SECRET_KEY = env("DJANGO_SECRET_KEY", default="django-insecure-sx83sr4c076gr9z5x#x$-#j0eela7az7jz_&81)6f&f80gygt3")

ALLOWED_HOSTS = ["localhost", "0.0.0.0","127.0.0.1"]