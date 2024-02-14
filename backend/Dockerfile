FROM python:latest

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY req.txt /code/

RUN pip install -r req.txt

COPY . /code/
