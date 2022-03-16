from datetime import timedelta
from prefect import Flow, task
from prefect.schedules import IntervalSchedule
from prefect.tasks.shell import ShellTask

@task(log_stdout=True)
def regular_task():
    print('hi')

my_shell_task = ShellTask(
    helper_script="cd ~",
)

with Flow(
    "My Flow",
    schedule=IntervalSchedule(interval=timedelta(minutes=2))

    
) as flow:
    # both tasks will be executed in home directory
    contents = my_shell_task(command='ls')

    regular_task()

if __name__ == "__main__":  
    flow.run()