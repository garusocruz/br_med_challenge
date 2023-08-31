# TODO: change from base tembici python base image
FROM python:3.10-slim-buster

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y -- \
    gettext \
    git \
    build-essential \
    libpq-dev

COPY poetry.toml poetry.toml
COPY pyproject.toml pyproject.toml
COPY currency_exchange currency_exchange
COPY exchange_rates exchange_rates
COPY manage.py manage.py
COPY .env .env

RUN pip install poetry
RUN poetry install
RUN python manage.py collectstatic

ENV PORT=8000
EXPOSE 8000

# CMD sh scripts/run_patient.sh
CMD ["gunicorn", "currency_exchange.wsgi:application"]
