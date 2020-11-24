ARG VERSION=3.8
FROM python:$VERSION-slim AS builder
RUN apt-get update && apt-get install -y libpq-dev gcc
ENV PYTHONUNBUFFERED=1
RUN mkdir /code
COPY . /code/
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ENTRYPOINT [ “python”, “manage.py”, “runserver”, "0.0.0.0:8000"]