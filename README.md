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

## Configuring DBT
For DBT it's necessary to update the parameter `host` from the profile.yml file.
The host is the ip of the docker network container above.

# All the notebook steps are in initial_state.ipynb

# If you find any issues contact me