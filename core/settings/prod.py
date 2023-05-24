from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ["text-to-image-production.up.railway.app"]

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL, conn_max_age=1800)
}

INSTALLED_APPS.append("whitenoise.runserver_nostatic")

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
