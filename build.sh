#!/bin/bash
python3.12 -m pip3 install --upgrade pip3
pip3 install psycopg2-binary
pip3 install -r requirements.txt
python3.12 manage.py collectstatic --no-input
