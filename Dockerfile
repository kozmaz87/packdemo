#Dockerfile
FROM python:3.7

RUN mkdir /application
WORKDIR "/application"

ADD le_demo/scripts/demo_script.py /application/

CMD [ "python", "demo_script.py" ]
