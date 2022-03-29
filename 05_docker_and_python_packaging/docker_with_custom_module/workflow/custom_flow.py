from prefect import flow, task

from components.componentA import ComponentA 
from components.componentB import ComponentB

@task
def custom_task():
    x = ComponentA(2)
    y = ComponentB(2)
    _sum = x.n + y.n
    print(f"Test {_sum}!")  # Should return 4
    return _sum

@flow
def custom_flow():
    custom_task()
