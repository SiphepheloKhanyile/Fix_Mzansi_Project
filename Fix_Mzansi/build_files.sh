#!/usr/bin/env bash
# build_files.sh
python pip install -r requirements.txt

sudo apt install curl -y

curl --create-dirs -o $HOME/.postgresql/root.crt "${CERT_URL}"

export DATABASE_URL="postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/fixmzansi_db?sslmode=verify-full"

# make migrations 
python manage.py migrate 
python manage.py collectstatic --no-input
