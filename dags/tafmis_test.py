import json
import requests
import pendulum


from airflow.decorators import dag, task

from commontasks import get_auth_token


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tafmis_test_data_fetch() -> dict:

    @task()
    def load(token: dict) -> None:

        print(f"{token}")


    token = get_auth_token(
        'https://api.ahe.r.mil.uk/connect/token',
        '1a23da3b-a7ac-4956-a1be-aafc31982a4f'
        '8446d903-f8f7-4d74-91bd-4453ae83395e',
        {'grant_type': 'client_credentials', 'scope': 'Mil-IndividualTraining_Access'}
    )

    load(token)


tafmis_test_data_fetch()
