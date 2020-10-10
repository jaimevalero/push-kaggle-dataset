FROM python:3.8

COPY . .
ADD . /app

RUN  pip install -r requirements.txt




ENTRYPOINT ["python" , "/entrypoint.py"]
