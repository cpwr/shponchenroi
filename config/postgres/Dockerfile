FROM postgres:10.6

RUN mkdir -p /docker-entrypoint-initdb.d
ADD bootstrap.sql /docker-entrypoint-initdb.d/
