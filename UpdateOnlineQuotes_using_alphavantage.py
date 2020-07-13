from alpha_vantage.timeseries import TimeSeries
from config import config
from datetime import datetime

import sys
import time
import logging


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
        cpt_retry= cpt_retry - 1
        log_function(logging.info, "One try to pull data ... {} remaining\n".format(cpt_retry))

        try:
            ts = TimeSeries(key=config.mAPIKey, output_format='pandas')
            data, meta_data = ts.get_daily(symbol=sys.argv[1],outputsize='compact')
            str_price = data['4. close'][0]
            cpt_retry = 0
        except:
            log_function(logging.warning, "ts.get_daily did not worked, trying ts.get_intraday\n")

            try:
                ts = TimeSeries(key=config.mAPIKey, output_format='pandas')
                data, meta_data = ts.get_intraday(symbol=sys.argv[1], outputsize='compact')
                str_price = data['4. close'][0]
                cpt_retry = 0
            except ValueError as error:
                log_function(logging.error, "Because of the 5 / minute API called limit ?\n")
                # Probably exceeded the API limit of 5 calls per minutes try again, recursively
                str_price = "0.00"
                time.sleep(60)
            except:
                log_function(logging.error, "ts.get_intraday failed Is it because of the 5 / minute API called limit ?\n")
                # Probably exceeded the API limit of 5 calls per minutes try again, recursively
                str_price = "0.00"
                time.sleep(60)

    print(str_price)



if __name__ == "__main__":
    main()
