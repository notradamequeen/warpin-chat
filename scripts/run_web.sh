#!/usr/bin/env bash

python manage.py createdb
python manage.py runserver --host '0.0.0.0'