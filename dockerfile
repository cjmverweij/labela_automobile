from python:3.6

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN sed -i "s/localhost/db/g" development.ini

RUN pip install --upgrade pip setuptools \
&& pip install --upgrade pip setuptools \
&& pip install -e ".[testing]"
