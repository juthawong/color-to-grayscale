FROM python:2.7

ADD . /app/code
WORKDIR /app/code

RUN pip install -r requirements.txt
