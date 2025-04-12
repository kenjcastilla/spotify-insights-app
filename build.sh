#!/bin/bash
python3.12 -m pip install --upgrade pip
pip install -r requirements.txt
python3.12 manage.py collectstatic --no-input
