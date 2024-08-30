import requests as r 
from bs4 import BeautifulSoup

def get_fx_to_inr(currency):
    url = f"https://www.google.com/finance/quote/{currency}-INR" 
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    inr_rate = soup.find("div", attrs={'data-last-price': True})
    rate = float(inr_rate['data-last-price'])
    return rate 
    


def get_stock_price_info(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    price_div = soup.find("div", attrs={'data-last-price': True})

    
    price = float(price_div['data-last-price'])
    currency_symbol= price_div['data-currency-code']

    inr_price = price
    if currency_symbol == "USD":
        rate = get_fx_to_inr(currency_symbol)
        inr_price = round(price * rate, 2)

    return {
        "ticker": ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency_symbol,
        "inr_price": inr_price
    } 

if __name__ =="__main__":
    print(get_stock_price_info('MSFT', 'NASDAQ'))
    print(get_stock_price_info('INFY', 'NSE'))
    print(get_stock_price_info('TSLA', 'NASDAQ'))
    print(get_stock_price_info('GOOG', 'NASDAQ'))
    print(get_stock_price_info('AAPL', 'NASDAQ'))
