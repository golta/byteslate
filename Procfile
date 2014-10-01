web: python manage.py runserver
worker: celery -A app.task worker --loglevel=info --concurrency=1 --beat