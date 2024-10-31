#!/bin/bash

rm db.sqlite3
rm -rf ./workflowapiapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations workflowapiapi
python3 manage.py migrate workflowapiapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

