from prefect import flow, task

# running on localhost
@task(name='trigger airbtye sync')
def trigger_airbyte_sync():
    pass

# running locally
@task(name='trigger dbt job')
def trigger_dbt_job():
    pass


@flow(name='My Basic Data Pipeline')
def my_flow():
    
    trigger_airbyte_sync()
    
    trigger_dbt_job()

if __name__ == "__main__":
    my_flow()