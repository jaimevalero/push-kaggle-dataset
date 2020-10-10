FROM python:3.8

COPY . .
ADD . /app

RUN  pip install -r /app/requirements.txt




ENTRYPOINT ["python" , "/app/entrypoint.py"]
