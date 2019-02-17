#!/usr/bin/env bash

set -e

PID=`ps -ef | grep gunicorn | grep -v grep | awk '{print $2}'`

if [[ "$PID" != "" ]]
then
    echo "Killing running gunicorn processes"
    pgrep -f gunicorn | xargs kill -9
fi

python manage.py makemigrations &&
python manage.py migrate &&
python manage.py collectstatic --no-input &&
gunicorn shponchenroi.wsgi:application --bind 0.0.0.0:8000 --workers=3 --reload
