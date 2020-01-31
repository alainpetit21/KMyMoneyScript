import sys
import time
from alpha_vantage.timeseries import TimeSeries
from config import config





def main():
    if len(sys.argv) < 2:
        print("Wrong format. Include a quote ID")

    str_price= ""

    try:
        ts = TimeSeries(key=config.mAPIKey, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=sys.argv[1],outputsize='compact')
        str_price = data['4. close'][0]
    except:
        try:
            ts = TimeSeries(key=config.mAPIKey, output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=sys.argv[1], outputsize='compact')
            str_price = data['4. close'][0]
        except:
            str_price = "0.00"

    time.sleep(5)

    print(str_price)



if __name__ == "__main__":
    main()
