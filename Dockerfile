#Pull official Base Image#(We use the alpine based Python Image to keep the final image slim)
FROM python:3.8.0-alpine

#Install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

#Set the Working Directory
WORKDIR /usr/src/app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTONBUFFERED 1

#Add and Install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#Add Entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh
#add app
COPY . .

#run server
CMD python manage.py run -h 0.0.0.0