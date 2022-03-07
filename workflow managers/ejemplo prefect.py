# from prefect import task, Flow
# import requests
# import json

# # extract
# @task
# def get_complaint_data():
#     r = requests.get("https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1/", params={'size':10})
#     json_response = json.loads(r.text)
#     return json_response['hits']['hits']

# # transform
# @task
# def parse_complaint_data(raw):
#     pass

# # load
# def store_complaints(parsed):
#     pass

# with Flow("coso") as f:
#     raw = get_complaint_data()
#     parsed = parse_complaint_data(raw)
#     store_complaints(parsed)
import csv
from prefect import task, Flow

@task
def extract(path):
    with open(path, "r") as f:
        text = f.readline().strip()
    data = [int(i) for i in text.split(",")]
    return data

@task
def transform(data):
    tdata = [i + 1 for i in data]
    return tdata

@task
def load(data, path):
    with open(path, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
    return

with Flow("coso") as flow:
    data = extract("values.csv")
    tdata = transform(data)
    print(tdata)
    load(tdata, "tvalues.csv")

#flow.visualize()
flow.run()