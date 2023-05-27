from dotenv import load_dotenv

load_dotenv()

from .base import *
import requests

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
SITE_ADDRESS = None


try: SITE_ADDRESS = requests.get("http://localhost:4040/api/tunnels").json()["tunnels"][0]["public_url"]
except: raise Exception("ngrok must be running to use webhook in local environment")
