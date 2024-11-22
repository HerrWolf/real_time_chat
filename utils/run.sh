python manage.py collectstatic --noinput
python manage.py migrate
gunicorn config.asgi --bind=0.0.0.0:80