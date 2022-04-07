#!/bin/sh


cd backend/bus_management_backend
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000 --settings=bus_management_backend.settings
