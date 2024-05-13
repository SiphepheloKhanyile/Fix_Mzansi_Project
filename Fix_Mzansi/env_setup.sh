#!/usr/bin/env bash
# Set Up Production Environment

sudo apt update
sudo apt install python3-venv python3-dev libpq-dev nginx curl

python3 -m venv Django_env
source Django_env/bin/activate

pip install django gunicorn psycopg2-binary
