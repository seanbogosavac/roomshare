#!/bin/bash
. venv/bin/activate 
export FLASK_APP=flaskr
export FLASK_ENV=development
clear
flask init-db
flask run
