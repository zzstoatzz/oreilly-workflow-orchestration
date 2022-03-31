from prefect import flow, task
from prefect.deployments import DeploymentSpec
from prefect.flow_runners import DockerFlowRunner

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

DeploymentSpec(
    name="docker-example",
    flow=custom_flow,
    flow_runner=DockerFlowRunner()
)

if __name__ == "__main__":
    custom_flow()