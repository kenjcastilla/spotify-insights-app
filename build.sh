#!/bin/bash
pip install -r requirements.txt
python3.12.9 manage.py collectstatic --no-input
