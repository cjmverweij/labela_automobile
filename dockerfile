from python:3.6

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED 0

RUN sed -i "s/localhost/db/g" development.ini

RUN pip install --upgrade pip setuptools
RUN pip install --upgrade pip setuptools
RUN pip install -e ".[testing]"
RUN python setup.py develop
