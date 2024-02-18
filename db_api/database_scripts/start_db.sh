#!/bin/bash

export FLASK_APP=app.py
flask db init
flask db migrate -m 'first migration'
flask db upgrade