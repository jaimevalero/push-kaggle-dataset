FROM python:3

WORKDIR /usr/src/app

COPY . .
RUN  pip3.8 install -r /usr/src/app/requirements.txt
CMD ["python" , "entrypoint.sh"]
