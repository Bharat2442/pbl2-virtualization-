from django.apps import AppConfig
from django.conf import settings
from django.contrib.auth import get_user_model
import logging


class ExpenseTrackerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense_tracker'

    def ready(self):
        # Avoid running this during migrations or tests
        import sys
        if 'runserver' not in sys.argv and 'gunicorn' not in sys.argv:
            return

        try:
            User = get_user_model()
            if not User.objects.filter(username=settings.DJANGO_SUPERUSER_USERNAME).exists():
                User.objects.create_superuser(
                    username=settings.DJANGO_SUPERUSER_USERNAME,
                    email=settings.DJANGO_SUPERUSER_EMAIL,
                    password=settings.DJANGO_SUPERUSER_PASSWORD
                )
                logging.info("Superuser created (from expense_tracker).")
            else:
                logging.info("Superuser already exists (from expense_tracker).")
        except Exception as e:
            logging.error(f"Error creating superuser in expense_tracker: {e}")
