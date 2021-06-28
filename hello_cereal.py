import requests
import csv
from dagster import pipeline, solid
from dagster import execute_pipeline
from time import sleep

@solid
def hello_cereal(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    sleep(4)
    context.log.info("----------------------start------------------")
    context.log.info(f"Found {len(cereals)} cereals")
    context.log.info("----------------------end------------------")


    return cereals

@pipeline
def hello_cereal_pipeline():
    hello_cereal()


if __name__ == "__main__":
    result = execute_pipeline(hello_cereal_pipeline)