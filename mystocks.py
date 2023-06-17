import locale
import yfinance as yahooFinance
locale.setlocale(locale.LC_ALL, 'en_US')

#List the stock symbols you want to view 
stocks = ["BA", "AMZN", "GIS"]

ticker = stocks[0]
 
for ticker in stocks:
    stockInfo = yahooFinance.Ticker(ticker) #Pull the stock info for each stock listed
    currentPrice = locale.currency(stockInfo.info[ 'currentPrice'], grouping=True) #Parse the current price and format for currency
    amtChange = locale.currency(((stockInfo.info[ 'currentPrice'] - stockInfo.info[ 'previousClose']))) # Subtract yesterdays close from todays close and format for currency
    perChange = ((stockInfo.info[ 'currentPrice'] / stockInfo.info[ 'previousClose'])-1) # calculate the percentage change between yesterday and today
    print("{: >8} {: >8} {: >8} {: >8} ".format(ticker, currentPrice,  amtChange, f"{perChange:.1%}"))# output the values and format the percentage change