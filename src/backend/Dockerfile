FROM python:3.5.2

MAINTAINER Mateusz Probachta <mateusz.probachta@pragmaticcoders.com>

RUN mkdir -p /app
ADD . /app

WORKDIR /app

EXPOSE 8080

RUN pip install -U pip && \
    pip install -r requirements.txt

CMD gunicorn --chdir backend_app backend_app.wsgi:application --bind 0.0.0.0:8080
