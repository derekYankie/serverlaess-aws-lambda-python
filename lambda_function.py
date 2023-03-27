import boto3
import json
import logging
import urllib3
import requests
from json import JSONDecodeError
from urllib.error import URLError, HTTPError
from ddtrace import tracer
from datadog_lambda.metric import lambda_metric
from datadog_lambda.wrapper import datadog_lambda_wrapper

http = urllib3.PoolManager()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def fetch_secret_value(secret_name):
    secrets_client = boto3.client("secretsmanager")
    response = secrets_client.get_secret_value(SecretId=secret_name, VersionStage='DECEMBER-23')
    
    return response

@datadog_lambda_wrapper
def lambda_handler(event, context):
    source = fetch_secret_value('CONVERT_API_SECRET')
    try:
        user_key = source['SecretString']
    except JSONDecodeError as json_err:
        logger.error("JSON Decode Error" + user_key,json_err.code)
        return "JSON Decode Error" + user_key
    
    url = 'https://v2.convertapi.com/user?Secret=%s'% (user_key)
    try:
        r = requests.get(url,timeout=3)
        r.raise_for_status()
        data = requests.get(url).text
    except requests.exceptions.ConnectionError as connection_errc:
        logger.error("Error Connecting:",connection_errc)
    except requests.exceptions.HTTPError as url_err:
        logger.error("Http Error: ", url_erre.code, url_err.reason)
    except requests.exceptions.Timeout as time_err:
        logger.error("Timeout Error:", time_err)
    except requests.exceptions.RequestException as req_err:
        logger.error("Request failed",req_err)
        
    data_obj = json.loads(data)
    seconds_left = data_obj['SecondsLeft']
    
    lambda_metric(
        metric_name = "convertapi.seconds_left",                  # Metric name
        value = seconds_left,                                    # Metric value
        tags = ['product:convertapi']                           # Associated tags
    )

