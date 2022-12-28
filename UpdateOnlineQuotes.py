from config import Config
from datetime import datetime

import requests
import sys
import time
import logging
import json


def log_function(whichFunction, message):
    txt_datetime = datetime.now()
    txt_datetime.strftime("%d/%m/%Y %H:%M:%S")
    message = "[" + str(txt_datetime) + "] " + message
    whichFunction(message)


def api_rapid_api(strQuote):
    response = None

    try:
        url = "https://real-time-finance-data.p.rapidapi.com/search"

        if strQuote[-3:] == ".TO":
            querystring = {"query": strQuote[:-3]}
        else:
            querystring = {"query": strQuote}

        headers = {
            "X-RapidAPI-Host": "real-time-finance-data.p.rapidapi.com",
            'x-rapidapi-key': Config.mAPIKey
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        dic_response = json.loads(response.text)

        str_price = dic_response["data"]["stock"][0]["price"]
        print(str_price)
        return True
    except:
        log_function(logging.warning, "Rapid API for Yahoo Finance did NOT WORK error :" + str(response.content))
        return False


def decisionTree(strQuote):
    return api_rapid_api(strQuote)


def main():
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)-15s %(clientip)s %(user)-8s %(message)s')

    if len(sys.argv) < 2:
        log_function(logging.critical, "Wrong format. Include a quote ID")
        return

    str_price = ""
    cpt_retry = 10

    while cpt_retry > 0:
        response = ""
        cpt_retry= cpt_retry - 1
        log_function(logging.info, "One try to pull data ... {} remaining\n".format(cpt_retry))

        if decisionTree(sys.argv[1]):
            cpt_retry = 0

        time.sleep(1)


if __name__ == "__main__":
    main()
