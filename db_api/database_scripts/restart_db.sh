#!/bin/bash

rm -rf migrations
rm data.sqlite

export FLASK_APP=app.py
flask db init
flask db migrate -m 'first migration'
flask db upgrade