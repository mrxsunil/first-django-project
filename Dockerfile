FROM python:3

ARG DJANGO_SUPERUSER_PASSWORD
ARG DJANGO_SUPERUSER_USERNAME
ARG DJANGO_SUPERUSER_EMAIL

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

# COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt && \
    python ./src/manage.py makemigrations && \
    python ./src/manage.py migrate && \
    echo -e "building the server"
    
RUN python ./src/manage.py createsuperuser --no-input --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL"

# COPY . /app

