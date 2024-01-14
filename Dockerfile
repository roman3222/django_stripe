FROM python:3.11-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /req/requirements.txt
COPY stripe_django /stripe_django
WORKDIR /stripe_django
EXPOSE 8000


RUN pip install -r /req/requirements.txt







