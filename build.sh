#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt


python manage.py create_superuser_if_not_exists


python manage.py collectstatic --no-input
python manage.py migrate