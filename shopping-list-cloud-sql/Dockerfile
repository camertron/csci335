FROM python:3.10-alpine

WORKDIR /usr/src/app

RUN apk update && apk add ca-certificates build-base mariadb-client mariadb-dev
RUN pip install --upgrade pip
RUN pip install flask flask-sqlalchemy mysqlclient

COPY web.py 01_create_database.sql 02_create_items.sql ./
COPY templates/ ./templates/

CMD ["python", "web.py"]

EXPOSE 5000
