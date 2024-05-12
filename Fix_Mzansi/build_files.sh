#!/usr/bin/env bash
# build_files.sh
python pip install -r requirements.txt

# make migrations 
python manage.py migrate 
python manage.py collectstatic --no-input
