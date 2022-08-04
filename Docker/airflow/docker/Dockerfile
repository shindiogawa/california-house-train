FROM python:3.9

RUN bash

RUN apt-get update -y &&\
    apt-get upgrade -y &&\
    apt-get install python3.9 -y &&\
    apt-get install python3-pip -y 

RUN apt-get install git -y

COPY ./requirements.txt /

RUN pip3 install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/root/airflow/

ENV AIRFLOW__CORE__EXECUTOR=LocalExecutor \
    AIRFLOW__CORE__SQL_ALCHEMY_CONN=postgresql+psycopg2://postgres:postgres@postgres:5432/cht \
    AIRFLOW__CORE__LOAD_EXAMPLES=False \
    AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS=False \
    AIRFLOW__CORE__FERNET_KEY=U26MSYEW6oQ7SqIjFUa6eW8SphFndHCUyURzwhvKHXs=

WORKDIR /usr/app/cht-dbt

EXPOSE 8080