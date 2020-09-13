from config import config
from datetime import datetime

import requests
import sys
import time
import logging
import json

def log_function(whichFunction, strMessage):
    strDateTime = datetime.now()
    strDateTime.strftime("%d/%m/%Y %H:%M:%S")
    strMessage = "[" + str(strDateTime) + "] " + strMessage
    whichFunction(strMessage)


def apiMorningStar(strQuote):
    response = None

    try:
        url = "https://morning-star.p.rapidapi.com/stock/v2/get-realtime-data"

        querystring = {"performanceId": strQuote}

        headers = {
            'x-rapidapi-host': "morning-star.p.rapidapi.com",
            'x-rapidapi-key': config.mAPIKey
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        dic_response = json.loads(response.text)

        str_price = dic_response["lastClose"]
        print(str_price)

        return True
    except:
        log_function(logging.warning, "Rapid API for Morning Star did NOT WORK error :" + str(response.content))
        return False


def apiYahooFinance(strQuote):
    response = None

    try:
        url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

        querystring = {"region": "US", "lang": "en", "symbols": strQuote}

        headers = {
            'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'x-rapidapi-key': config.mAPIKey
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        dic_response = json.loads(response.text)

        str_price = dic_response["quoteResponse"]["result"][0]["regularMarketPrice"]
        print(str_price)
        return True

    except:
        log_function(logging.warning, "Rapid API for Yahoo Finance did NOT WORK error :" + str(response.content))
        return False


def decisionTree(strQuote):
    if(strQuote == "0P000072TQ"):
        return apiMorningStar(strQuote)

    elif(strQuote == "0P0000715V"):
        return apiMorningStar(strQuote)

    elif(strQuote == "0P0000715P"):
        return apiMorningStar(strQuote)

    else:
        return apiYahooFinance(strQuote)


def main():
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)-15s %(clientip)s %(user)-8s %(message)s')

    if len(sys.argv) < 2:
        log_function(logging.critical, "Wrong format. Include a quote ID")
        return

    str_price= ""
    cpt_retry = 10

    while cpt_retry > 0:
        response = ""
        cpt_retry= cpt_retry - 1
        log_function(logging.info, "One try to pull data ... {} remaining\n".format(cpt_retry))

        if(decisionTree(sys.argv[1])):
            cpt_retry = 0

        time.sleep(1)



if __name__ == "__main__":
    main()
