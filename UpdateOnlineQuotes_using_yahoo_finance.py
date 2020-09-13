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

        try:
            url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-quotes"

            querystring = {"region": "US", "lang": "en", "symbols": sys.argv[1]}

            headers = {
                'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
                'x-rapidapi-key': config.mAPIKey
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            dic_response = json.loads(response.text)

            str_price = dic_response["quoteResponse"]["result"][0]["regularMarketPrice"]
            cpt_retry = 0
        except:
            log_function(logging.warning, "Rapid API for Yahoo Finance did NOT WORK error :" + response.content)

        time.sleep(1)

    print(str_price)



if __name__ == "__main__":
    main()
