from prefect import flow, task

import json, requests, subprocess, time

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# running on EC2, port forwarded into via public IP
@task(name='trigger airbtye sync')
def trigger_airbyte_sync(connectionId: str) -> bool:
    try:
        response = requests.post(
            url='http://localhost:8000/api/v1/connections/sync',
            headers=headers,
            data=json.dumps({"connectionId": connectionId})
        )
        assert response.ok

        job_id = response.json()["job"]["id"]
        job_status = ''
        
        while job_status != 'succeeded':
            job_response = requests.post(
                url='http://localhost:8000/api/v1/jobs/get/',
                headers=headers,
                data=json.dumps({"id": job_id})
            )
            
            job_status = job_response.json()["job"]["status"]
            print(job_status)
            time.sleep(5)
        
        return True
    
    except AssertionError:
        print('Bad Response')
        return None
    
# dbt running locally, connected to my snowflake instance
@task(name='trigger dbt job')
def trigger_dbt_job(dbt_command: str) -> None:
        
    subprocess.run(dbt_command.split())

@flow(name='My Basic Data Pipeline')
def my_flow(airbyte_connection_id: str, dbt_command: str) -> None:
    
    result = trigger_airbyte_sync(airbyte_connection_id)

    if result.result():
        trigger_dbt_job(dbt_command)

if __name__ == "__main__":
    
    airbyte_connection_id = 'e1b2078f-882a-4f50-9942-cfe34b2d825b'
    dbt_command = 'dbt run --project-dir dbt_demo'
    
    my_flow(
        airbyte_connection_id, 
        dbt_command
    )