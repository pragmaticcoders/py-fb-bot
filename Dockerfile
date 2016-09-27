FROM python:3.5.2

MAINTAINER Mateusz Probachta <mateusz.probachta@pragmaticcoders.com>

RUN mkdir -p /app
ADD ./src /app/src
ADD ./requirements.txt /app

WORKDIR /app

EXPOSE 8080

RUN pip install -U pip && \
    pip install -r requirements.txt

CMD gunicorn src.runner:app --bind 0.0.0.0:8080 --worker-class aiohttp.worker.GunicornWebWorker -w 6
