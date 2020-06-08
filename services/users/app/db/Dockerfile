#Docker File for PostGres
#Pulls the official Base Image
FROM postgres:12.1-alpine

#Run Create sql on Init
ADD create.sql /docker-entrypoint-initdb.d
