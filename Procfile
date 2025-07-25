release: python manage.py migrate
web: gunicorn theatre_blog.wsgi:application --bind 0.0.0.0:$PORT --log-file -