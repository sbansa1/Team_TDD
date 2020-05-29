#!/bin/sh
#Entry ,sh makes sure that the instance of the Database or postgres databse it up and healthy and is running.
echo "waiting for Postgress ......!"

while ! nc -z users-db 5432; do
   sleep 0.1
done

echo "PostgreSQL Server Started...."

python manage.py run -h 0.0.0.0
