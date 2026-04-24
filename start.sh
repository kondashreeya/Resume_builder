python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn resume_bilder.wsgi:application --bind 0.0.0.0:$PORT 