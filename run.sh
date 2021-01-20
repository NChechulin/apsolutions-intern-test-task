#!/usr/bin/bash

docker build -t apsolutions-intern-test-task:latest .
docker run -d -p 5000:5000 --name apsolutions-intern-test-task --rm apsolutions-intern-test-task:latest
