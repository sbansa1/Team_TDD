FROM python:3.8.0-alpine

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

COPY ./requrirements.txt /usr/src/app/requrirements.txt
RUN pip install -r requrirements.txt

COPY . .

CMD python manage.py run -h 0.0.0.0