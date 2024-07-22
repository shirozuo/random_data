@echo off
start cmd /k "daphne -p 8000 random_data.asgi:application"
start cmd /k "python manage.py runserver"
start cmd /k "python scheduler.py"
