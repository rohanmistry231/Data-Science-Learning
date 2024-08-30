import pandas as pd
import requests
import plotly.graph_objects as pg
import plotly.io as pio




print("""Program entirely dependent on API's reponse.
        Commands:
        Type "IS" followed by ticker symbol for Income statement.(IS AAPL)
        Type "divs" followed by ticker symbol for dividends.(divs AAPL)
        Type "prices" followed by ticker symbol for historical prices with a graph.(prices AAPL)
        Type "profile" followed by ticker symbol for company profile.(profile AAPL)
        Type "quotes" followed by ticker symbol for todays stock details.(quotes AAPL)
        Type "ratios" followed by ticker symbol for todays stock ratios.(ratios AAPL)
        Type "growth" followed by ticker symbol for todays stock last year growth.(growth AAPL)
     """)
api_key = "**************************"



def income_statement(stock):
  try:
      number_qts = input("Number of quarters: ").strip()
      IS = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{stock.upper()}?limit={number_qts}&apikey={api_key}").json()
      IS = pd.DataFrame.from_dict(IS)
      IS = IS.T
      print(IS)
      save_to_csv= input("Save to a csv file? y or n:  ").strip()
      if save_to_csv == 'y':
          IS.to_csv('data.csv')
      else:
        pass
  except Exception:
      print("Not avilable!")





def dividends(stock):
    number_of_dividends = input("Enter number of dividends? ").strip()
    number_of_dividends = int(number_of_dividends)
    try:
      dividends = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/stock_dividend/{stock}?apikey={api_key}").json()
      dividends = dividends['historical'][0:4]

      for item in dividends:
          print(f"{item['paymentDate']} : Dividends was : {str(item['dividend'])}")
    except Exception:
      print(f"Data not avilable for {stock}")


def historicalPrices(stock):
    hist_prices = requests.get(f"https://financialmodelingprep.com/api/v3/historical-price-full/{stock}?apikey={api_key}").json()
    hist_prices = hist_prices['historical']
    price_data = {    }

    for item in hist_prices:
        price_data[item['date']] = {}
        price_data[item['date']]['date'] = item['date']
        price_data[item['date']]['open'] = item['open']
        price_data[item['date']]['high'] = item['high']
        price_data[item['date']]['low'] = item['low']
        price_data[item['date']]['adjClose'] = item['adjClose']

    price_df = pd.DataFrame.from_dict(price_data)
    price_df = price_df.T
    print(f"Stock Ticker: {stock.upper()}\n\n{price_df.head(10)}")
    print("Generating Graph.. .")
   
    pio.renderers.default = 'browser'
    fig = pg.Figure(data=[pg.Candlestick        (x=price_df['date'],
                    open=price_df['open'],
                    high=price_df['high'],
                    low=price_df['low'],
                    close=price_df['adjClose'])])

    # fig.write_image("prices.png")
    fig.show()
    


def profile(stock):
    company_profile = requests.get(f"https://financialmodelingprep.com/api/v3/profile/{stock}?apikey={api_key}").json()

    for item in company_profile:
        print(f"""Symbol:{item['symbol']}
            Company Name: {item['companyName']}
            Currency: {item['currency']}
            Current Price: {item['price']}
            Market Cap: {item['mktCap']}
            Company Beta: {item['beta']}
            Last Dividend: {item['lastDiv']}

            Exchange: {item['exchange']}
            Website: {item['website']}
            Industry: {item['industry']}
            CEO: {item['ceo']}
            Country: {item['country']}
            DCF: {item['dcf']}
            Is Actively Trading: {item['isActivelyTrading']}
        """)


def todayQuote(stock):
    quotes = requests.get(f"https://financialmodelingprep.com/api/v3/quote/{stock.upper()}?apikey={api_key}").json()
    
    try:
        for item in quotes:
            print(f"""Blank if API doesn't allow!
            Company Name: {item['Company Name']}
            Current Price: {item['price']}
            Today's Open: {item['previousCpen']}
            Previous Day Close: {item['close']}
            Price change(%): {item['changesPercentage']}
            Price Change($): {item['change']}
            Today's Low: {item['dayLow']}
            Today's High: {item['dayHigh']}
            Year's Low: {item['yearLow']}
            Year's High: {item['yearHigh']}
            Market Cap: {item['marketCap']}
            Price Average(50 days): {item['priceAvg50']}
            Total Volume: {item['volume']}\n 
            Earning Per Share: {item['eps']}
            Price to Earnings: {item['pe']}
            Shares outstanding: {item['sharesOutstanding']}
            """)
    except Exception:
        print("Quotes not avialble right now!")


def financialRatios(stock):
    ratios = requests.get(f"https://financialmodelingprep.com/api/v3/ratios-ttm/{stock}?apikey={api_key}").json()

    for item in ratios:
        print(f"""None If not avialble\n
        Dividend Per Share: {item['dividendPerShareTTM']} 
        Price Earning Ratio: {item['priceEarningsRatioTTM']}
        Return on Equity: {item['returnOnEquityTTM']}
        Debt Ratio: {item['debtRatioTTM']}
        Debt Equity: {item['debtEquityRatioTTM']}
        Net Profil Margin: {item['netProfitMarginTTM']}
        
        PE Ratio: {item['peRatioTTM']}
        PEG Ratio: {item['pegRatioTTM']}
        
        Price Fair Value: {item['priceFairValueTTM']}
        """)



# def recentNews(stock):
#     news = requests.get(f"https://financialmodelingprep.com/api/v4/articles?page=0&size=5?tickers={stock.upper()}&apikey={api_key}").json()
#     print(news)
#     for item in news:
#         print(f"""Title: {item['title']}
#          Website: {item['site']}
#          Description: {item['text']}
#          Link: {item['url']}
#         """)


def financialGrowth(stock):
    growth=requests.get(f"https://financialmodelingprep.com/api/v3/financial-growth/{stock.upper()}?limit=1&apikey={api_key}").json()

    for item in growth:
        print(f""" Revenue Growth: {item['revenueGrowth']}
        EPS Growth:{item['epsgrowth']}
        Net Income Growth: {item['netIncomeGrowth']}
        Debt Growth: {item['debtGrowth']}
        Dividend Per Share Growth: {item['dividendsperShareGrowth']}
        Operating Income Growth: {item['operatingIncomeGrowth']}
        Free Cash Flow growth: {item['freeCashFlowGrowth']}
        """)





while True:
  try:
    comman = input("Enter Stock ticker? ")
    stock = comman.split(" ")[1]

    if comman == "IS " + stock:
        income_statement(stock)

    if comman == "divs " + stock:
        dividends(stock)

    if comman == "prices " + stock:
        historicalPrices(stock)

    if comman == "profile " + stock:
        profile(stock)

    if comman == "quotes " + stock:
        todayQuote(stock)

    if comman == "ratios " + stock:
        financialRatios(stock)

    # if comman == "news " + stock:
    #     recentNews(stock)

    if comman == "growth " + stock:
        financialGrowth(stock)

    elif comman =='quit':
        break
  except KeyboardInterrupt:
    print("No command!")

