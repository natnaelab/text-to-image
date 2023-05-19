from .base import *
import dj_database_url, os

DEBUG = False

ALLOWED_HOSTS = [""]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL")
    )
}


MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')


STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
