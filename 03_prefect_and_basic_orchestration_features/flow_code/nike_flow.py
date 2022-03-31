from prefect import flow, task
from prefect_slack import SlackWebhook
from prefect_slack.messages import send_chat_message
from prefect.tasks import task_input_hash
from datetime import timedelta
import requests
import re
from bs4 import BeautifulSoup

@task(retries=3, retry_delay_seconds=10)
def find_nike_price(url):
    k = requests.get(url).text
    soup = BeautifulSoup(k,'html.parser')
    price_string = soup.find('div', {"class":"product-price"}).text
    price_string = price_string.replace(' ','')
    price = int(re.search('[0-9]+',price_string).group(0))
    return price

@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def compare_price(price, budget):
    if price <= budget:
        return "Buy the shoes! Good deal!"
    else:
        return "Don't buy the shoes. They're too expensive"

@flow(name="Shoe Price Notification")
def nike_flow(url: str, budget: int, slack_token: str):
    price = find_nike_price(url)
    message = compare_price(price, budget)
    send_chat_message(
        slack_credentials=SlackWebhook(slack_token),
        text=f"{message}"
   )


url = "https://www.nike.com/t/air-max-270-womens-shoes-Pgb94t/AH6789-601"
budget = 120
slack_token = 'https://hooks.slack.com/services/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'
    
nike_flow(url, budget, slack_token)

from prefect.deployments import DeploymentSpec
from prefect.orion.schemas.schedules import IntervalSchedule
from datetime import timedelta

DeploymentSpec(
    flow=nike_flow,
    name="Nike Shoe Flow",
    schedule=IntervalSchedule(interval=timedelta(days=1)),
    tags=["demo"]
)