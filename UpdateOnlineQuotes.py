from requests_html import HTMLSession
import sys
import re


def canUse_GlobeAndMailFunds_Strategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "LLI108.CF":
        isWorking= True

    if strInput == "LLI207.CF":
        isWorking = True

    if strInput == "LLI204.CF":
        isWorking = True

    return isWorking



def canUse_YahooFinance_Strategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "F0CAN05MT3.TO":
        isWorking= True

    if strInput == "F0CAN05MT9.TO":
        isWorking = True

    if strInput == "F0CAN05OH4.TO":
        isWorking = True

    return isWorking


def canUse_MorningStarDotCa_Strategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "F0CAN05MT3":
        isWorking= True

    if strInput == "F0CAN05MT9":
        isWorking = True

    if strInput == "F0CAN05OH4":
        isWorking = True

    return isWorking


def canUse_MarketPlaceStocks_Strategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "MNKD":
        isWorking= True
    if strInput == "IRM":
        isWorking= True

    return isWorking


def canUse_MarketPlaceFunds_Strategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "VXUS":
        isWorking= True
    if strInput == "VUN":
        isWorking= True
    if strInput == "VAB":
        isWorking= True
    if strInput == "VTI":
        isWorking= True
    if strInput == "TKC":
        isWorking= True
    if strInput == "SJR":
        isWorking= True
    if strInput == "OSTK":
        isWorking= True
    if strInput == "HYGS":
        isWorking= True
    if strInput == "HQL":
        isWorking= True
    if strInput == "HQH":
        isWorking= True
    if strInput == "FB":
        isWorking= True
    if strInput == "ERX":
        isWorking= True
    if strInput == "EE":
        isWorking= True
    if strInput == "DIA":
        isWorking= True

    return isWorking


def canUse_GlobeAndMailETF_Strategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "ZRE-T":
        isWorking = True
    if strInput == "XRB-T":
        isWorking = True
    if strInput == "XIC-T":
        isWorking = True
    if strInput == "XEF-T":
        isWorking = True
    if strInput == "XEC-T":
        isWorking = True
    if strInput == "XBB-T":
        isWorking = True
    if strInput == "XIC-T":
        isWorking = True
    if strInput == "XIC-T":
        isWorking = True
    if strInput == "XIC-T":
        isWorking = True

    return isWorking


def canUseGlobeAndMailStockStrategy(strInput):
    """Just to make sure that we have it tested"""

    isWorking = False

    if strInput == "XIN-N":
        isWorking = True
    if strInput == "TCT-UN-T":
        isWorking = True

    return isWorking


def main():
    if len(sys.argv) < 2:
        print("Wrong format. Include a quote ID")

    hasAStrategy = False
    strPrice = ""
    url = ""
    xpathPattern = ""
    xpathPattern2 = ""
    testTxt = ""

    if canUse_MorningStarDotCa_Strategy(sys.argv[1]):
        url = "http://quote.morningstar.ca/quicktakes/fund/f_ca.aspx?t=" + sys.argv[1]
        xpathPattern = '//*[@id="idPrice"]/div[2]/div[1]/div[2]/div/text()'
        xpathPattern2 = xpathPattern
        hasAStrategy = True

    elif canUse_MarketPlaceFunds_Strategy(sys.argv[1]):
        url = "https://www.marketwatch.com/investing/fund/" + sys.argv[1]
        xpathPattern = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/h3/span/text()'
        xpathPattern2 = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/h3/bg-quote/text()'
        hasAStrategy = True

    elif canUse_MarketPlaceStocks_Strategy(sys.argv[1]):
        url = "https://www.marketwatch.com/investing/stock/" + sys.argv[1]
        xpathPattern = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/h3/bg-quote/text()'
        xpathPattern2 = '/html/body/div[2]/div[2]/div[2]/div/div/div[2]/h3/span/text()'
        hasAStrategy = True

    elif canUse_YahooFinance_Strategy(sys.argv[1]):
        url = "https://finance.yahoo.com/quote/" + sys.argv[1]
        xpathPattern = '//*[@id="quote-header-info"]/div[3]/div/div/span[1]/text()'
        xpathPattern2 = xpathPattern
        hasAStrategy = True

    elif canUse_GlobeAndMailETF_Strategy(sys.argv[1]):
        url = "https://www.theglobeandmail.com/investing/markets/stocks/" + sys.argv[1]
        xpathPattern = '//*[@id="etfsDetail"]/div[1]/span[2]/span[2]/barchart-field/text()'
        xpathPattern2 = '//*[@id="etfsDetail"]/div[1]/span[2]/span[2]/barchart-field/@value'
        hasAStrategy = True

    elif canUseGlobeAndMailStockStrategy(sys.argv[1]):
        url = "https://www.theglobeandmail.com/investing/markets/stocks/" + sys.argv[1]
        xpathPattern = '//*[@id="stocksDetail"]/div[1]/span[2]/span[2]/barchart-field/text()'
        xpathPattern2 = xpathPattern
        hasAStrategy = True

    elif canUse_GlobeAndMailFunds_Strategy(sys.argv[1]):
        url = "https://www.theglobeandmail.com/investing/markets/funds/" + sys.argv[1]
        xpathPattern = '//*[@id="fundsDetail"]/div[1]/span[2]/span[2]/barchart-field/text()'
        xpathPattern2 = '//*[@id="fundsDetail"]/div[1]/span[2]/span[2]/barchart-field/@value'
        hasAStrategy = True

    else:
        print("No Update strategy found for" + sys.argv[1])
        #Maybe try to implement a default strategy
#alphaventage.co key H86X2ITIWPCFN5SW


    if(hasAStrategy):
        #Execute the strategy
        session = HTMLSession()
        resp = session.get(url)

        if (resp.status_code == 200):
            resp.html.render()
            node = resp.html.xpath(xpathPattern)
            if len(node) != 0:
                testTxt = node[0]

            #if pattern 1 does not work try pattern 2
            if len(testTxt) == 0:
                node = resp.html.xpath(xpathPattern2)
                if len(node) != 0:
                    testTxt = node[0]

            #if ends in full number 26.00
            if "." not in testTxt:
                testTxt= testTxt + ".00"

            lstStrPrice = re.findall(r'(\d+\.\d+)', testTxt)
            strPrice= lstStrPrice[0]

        print(strPrice)


if __name__ == "__main__":
    main()
