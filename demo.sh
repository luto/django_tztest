#!/bin/sh -e

python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

docker-compose up -d
sleep 3s
cd tztest
./manage.py migrate
./manage.py tztest
