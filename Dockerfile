FROM python:3.8.10-slim-buster

RUN pip install -U pip wheel pip-tools

ENV SOURCE /var/myproject
RUN mkdir -p $SOURCE
WORKDIR $SOURCE
COPY . .
