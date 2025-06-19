web: gunicorn todo_exptrack.wsgi:application --bind [::]:8080
release: python manage.py collectstatic --noinput
release: python manage.py createsuperuser --noinput