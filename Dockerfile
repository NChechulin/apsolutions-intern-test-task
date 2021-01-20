FROM python:latest

WORKDIR /home/apsolutions-intern-test-task

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY intern_task.py .
COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP apsolutions-intern-test-task.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]
