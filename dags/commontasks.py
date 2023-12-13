import requests 
import json

from airflow.decorators import dag, task

@task(multiple_outputs=True)
def get_auth_token(
        url: str,
        client_id: str,
        client_secret: str,
        data: dict
) -> dict:
    access_token_response = requests.post(url,
                                        data=data,
                                        verify=False,
                                        allow_redirects=False,
                                        auth=(client_id, client_secret))
    token = json.loads(access_token_response.text)
    return token
    

