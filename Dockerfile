FROM python:3.8

ADD . /app

RUN  pip install -r /app/requirements.txt


LABEL "com.github.actions.icon"="upload-cloud"
LABEL "com.github.actions.color"="blue"

ENTRYPOINT ["python" , "/app/entrypoint.py"]
