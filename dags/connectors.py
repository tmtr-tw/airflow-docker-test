import json

from airflow.models.connection import Connection

airflow_db = Connection(
    conn_id="airflow_db",
    conn_type="postgresql",
    description="Postgres instance used as the airflow backend",
    host="postgres",
    login="postgres",
    password="postgres"
)

tafmis_api = Connection(
    conn_id="tafmis",
    conn_type="http",
    scheme="https",
    
)