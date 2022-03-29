from prefect import flow, task

import json, requests, subprocess, time

airbyte_base_url = f'http://localhost:8000/api'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# running on EC2
@task(name='trigger airbtye sync')
def trigger_airbyte_sync(connectionId: str) -> bool:
    try:
        # response = requests.post(
        #     url=airbyte_base_url+'/v1/connections/sync',
        #     headers=headers,
        #     data=json.dumps({"connectionId": connectionId})
        # )
        
        # assert response.ok
        print('Waiting for airbyte sync to complete...')
        time.sleep(5)
        return True
    
    except AssertionError:
        print('Bad Response')
        return None
    
# running locally
@task(name='trigger dbt job')
def trigger_dbt_job(dbt_command: str) -> None:
        
    subprocess.run(dbt_command.split())

@flow(name='My Basic Data Pipeline')
def my_flow(airbyte_connection_id: str, dbt_command: str) -> None:
    
    result = trigger_airbyte_sync(airbyte_connection_id)
        
    if result:
        trigger_dbt_job(dbt_command)

if __name__ == "__main__":
    
    airbyte_connection_id = 'ee48c189-33e9-4cf1-b6e6-2047e20f5739'
    dbt_command = 'dbt run --project-dir dbt_demo'
    
    my_flow(
        airbyte_connection_id, 
        dbt_command
    )