FROM python:3.5.2

MAINTAINER Mateusz Probachta <mateusz.probachta@pragmaticcoders.com>

EXPOSE 8080

RUN mkdir -p /app
WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

ADD . /app

CMD bash -c "\
  export DATABASE_URL=postgresql://$RDS_USERNAME:$RDS_PASSWORD@$RDS_HOSTNAME:$RDS_PORT/$RDS_DB_NAME && \
  python backend_app/manage.py migrate && \
  gunicorn --chdir backend_app backend_app.wsgi:application --bind 0.0.0.0:8080"
