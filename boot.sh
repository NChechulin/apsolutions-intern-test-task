#!/bin/sh
. venv/bin/activate
exec gunicorn -b :5000 --access-logfile - --error-logfile - intern_task:app
