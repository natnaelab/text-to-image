release: python manage.py migrate --settings=core.settings.prod
web: gunicorn 'core.wsgi' --log-file -