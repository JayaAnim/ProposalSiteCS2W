FROM alpine:3.17

ARG DEBIAN_FRONTEND="noninteractive"
ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache \
    python3 py3-pip build-base

WORKDIR /app

RUN apk add --no-cache python3-dev

ADD requirements.txt /app/
RUN python3 -m pip install -r requirements.txt

ADD . /app/

CMD python3 manage.py runserver 0.0.0.0:8000
