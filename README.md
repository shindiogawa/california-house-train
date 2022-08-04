# California House Traning Project - by Rodrigo Ogawa

## This is a mini ELT project where I'm using the following technologies:
1. Docker (docker-compose)
2. Jupyther notebook using pyspark
3. Github
4. DBT (Data Build Tool)
5. Airflow
6. PostgreSQL and PgAdmin

### Steps to make this project working NICE!

Access the folder `Docker` and run
```bash
docker-compose up
```
Pay Attention to the log when you run `docker-compose up`, because there you will see the token to access jupyther notebook.
The folder `jupyther` has the notebook with the scripts to ingest data into the postgres database and consume from the csv file.

<img width="531" alt="image" src="https://user-images.githubusercontent.com/29340376/182907473-55a33651-d134-4c45-9d10-34e42ee57c40.png">


It's necessary to update the `POSTGRES_DB_IP`, to update , open a new terminal and run:
```bash
docker inspect network docker_network-common
```
the IP of your database will be the "Gateway" inside this object:
```json
"IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.18.0.0/16",
                    "Gateway": "172.18.0.1"
                }
            ]
        }
```

In this case the internal ip of the container is `172.18.0.1`.

## Accessing POSTGRES DB using PG Admin
to access the PG Admin you can open
`http://localhost:5050` in your prefered browser

The default password is `admin`

You need to create a server.
In my case I created one called `california_house_training` inside `Servers`
The db is `cht` and the table to ingest the csv file is `cht_raw`

![image](https://user-images.githubusercontent.com/29340376/182907388-a3a074ff-73e2-4a85-9b9e-43e7ffe962f2.png)


## Configuring DBT
For DBT it's necessary to update the parameter `host` from the profile.yml file.
The host is the ip of the docker network container above.

# PostgreSQL and PgAdmin Docker Compose

## Requirements:
* docker >= 17.12.0+
* docker-compose

## User Guide
* In the terminal go to the directory `cd edw`
* It is necessary to create an .env file inside `airflow/` with the variables `AWS_REGION, BUCKET_AWS_ACCESS_KEY_ID ,BUCKET_AWS_SECRET_ACCESS_KEY`
* Run `docker-compose up`
* Check jupyter_notebook log to access with token

## Environment variables
* `POSTGRES_USER` default **postgres**
* `POSTGRES_PASSWORD` default **postgres**
* `PGADMIN_PORT` default **5050**
* `PGADMIN_DEFAULT_EMAIL` default **pgadmin4@pgadmin.org**
* `PGADMIN_DEFAULT_PASSWORD` default **admin**
* `ENV AIRFLOW__CORE__EXECUTOR` LocalExecutor`
* `AIRFLOW__CORE__SQL_ALCHEMY_CONN` postgresql+psycopg2://${POSTGRES_HOST}:${POSTGRES_USER}@${POSTGRES_PASSWORD}:5432/${POSTGRES_DATABASE}
* `AIRFLOW__CORE__LOAD_EXAMPLES` False
* `AIRFLOW__CORE__LOAD_DEFAULT_CONNECTIONS` False
* `AIRFLOW__CORE__FERNET_KEY` ${generate_fernet_key.py}
* `AWS_REGION` **region-aws**
* `BUCKET_AWS_ACCESS_KEY_ID` **s3-aws-access-key-id**
* `BUCKET_AWS_SECRET_ACCESS_KEY` **s3-aws-secret-access-key**
## Access Postgres:
* `localhost:5432`
* **User:** postgres (default)
* **Password:** postgres (default)

## Access PgAdmin:
* **URL:** `http://localhost:5050`
* **User:** pgadmin4@pgadmin.org (default)
* **Password:** admin (default)

## Access Airflow:
* **URL:** `http://localhost:8080`
* **User:** airflow (default)
* **Password:** airflow (default)

## Add server in PgAdmin:
* **Host** `postgres`
* **Port** `5432`
* **User** `POSTGRES_USER`, default: `postgres`
* **Password** `POSTGRES_PASSWORD`, default `postgres`

![image](https://user-images.githubusercontent.com/29340376/182907757-45a8ac16-0388-4616-8ae1-e97724a9fdb0.png)




# All the notebook steps are in initial_state.ipynb

# If you find any issues contact me
