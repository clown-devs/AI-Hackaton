FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /AI_Bot

RUN pip install --upgrade pip
COPY ./bot/requirements.txt /AI_Bot/
COPY ./bot/.env /AI_Bot/
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN pip install -r requirements.txt
COPY . .