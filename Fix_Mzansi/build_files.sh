#!/usr/bin/env bash
# build_files.sh
pip install -r requirements.txt
curl --create-dirs -o $HOME/.postgresql/root.crt 'https://cockroachlabs.cloud/clusters/f7afce05-224c-48ff-a0bb-9739c97439eb/cert'
# make migrations
python3.9 manage.py makemigrations 
python3.9 manage.py migrate 
python3.9 manage.py collectstatic --no-input
