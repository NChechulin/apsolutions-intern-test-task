#!/bin/sh
. venv/bin/activate
exec gunicorn -b :$APPLICATION_PORT --access-logfile - --error-logfile - intern_task:app
