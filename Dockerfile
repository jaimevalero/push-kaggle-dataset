FROM python:3.8

ADD . /app

RUN  pip install -r /app/requirements.txt




ENTRYPOINT ["python" , "/app/entrypoint.py"]
