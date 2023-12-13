import json
import requests
import pendulum


from airflow.decorators import dag, task


@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def tafmis_test_data_fetch() -> dict:

    
    @task(multiple_outputs=True)
    def get_token():
        token_url = 'https://api.ahe.r.mil.uk/connect/token'
        client_id = '1a23da3b-a7ac-4956-a1be-aafc31982a4f'
        client_secret = '8446d903-f8f7-4d74-91bd-4453ae83395e'
        data_creds = {'grant_type': 'client_credentials', 'scope': 'Mil-IndividualTraining_Access'}
        access_token_response = requests.post(token_url,
                                           data=data_creds,
                                           verify=False,
                                           allow_redirects=False,
                                           auth=(client_id, client_secret))
        token = json.loads(access_token_response.text)
        return token
    
    
    @task()
    def load(token: dict) -> None:

        print(f"{token}")


    token = get_token()
    load(token)


tafmis_test_data_fetch()
