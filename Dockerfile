FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

# COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt && \
    python ./src/manage.py makemigrations && \
    python ./src/manage.py migrate && \
    echo -e "building the server"
    


# COPY . /app

