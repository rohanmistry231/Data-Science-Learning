import cryptocompare
import requests
import tkinter as tk
from datetime import datetime

# fetching data from crypto compare API
def trackcryptoprice():
    url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH&tsyms=USD,INR"
    res = requests.get(url).json()
    
    # usd and inr price for btc
    price_btc_usd = res['BTC']['USD']
    price_btc_inr = res['BTC']['INR']

    # usd and inr price for eth
    price_eth_usd = res['ETH']['USD']
    price_eth_inr = res['ETH']['INR']

    # time and date
    time = datetime.now().strftime("%H:%M:%S")
    today = datetime.today().strftime('%Y-%m-%d')

    # Inserting data into tkinter window
    labelpriceBTCUSD.config(text = str(price_btc_usd) + ' $')
    labelpriceBTCINR.config(text = str(price_btc_inr) + ' ₹')

    labelpriceETHUSD.config(text = str(price_eth_usd) + ' $')
    labelpriceETHINR.config(text = str(price_eth_inr) + ' ₹')

    labeltime.config(text = 'Updated at: '+ time + ' '+ 'Date: '+ today)

    # updateing time every second
    win.after(1000, trackcryptoprice)


# creating a window with tkinter
win  = tk.Tk()
win.geometry("500x680")
win.title("Crypto Currency Tracker")

f1 = ("poppins", 20, "bold ")
f2 = ("poppins", 18, "bold underline")
f3 = ("poppins", 20, "normal")

label = tk.Label(win, text = "Current Price", font=f1)
label.pack(pady = 20)

label = tk.Label(win, text = "BTC", font=f2)
label.pack(pady = 16)

labelpriceBTCUSD = tk.Label(win, font=f3)
labelpriceBTCUSD.pack(pady = 20)

labelpriceBTCINR = tk.Label(win, font=f3)
labelpriceBTCINR.pack(pady = 20)

label = tk.Label(win, text = "ETH", font=f2)
label.pack(pady = 16)

labelpriceETHUSD = tk.Label(win, font=f3)
labelpriceETHUSD.pack(pady = 20)

labelpriceETHINR = tk.Label(win, font=f3)
labelpriceETHINR.pack(pady = 20)

labeltime = tk.Label(win, font=f3)
labeltime.pack(pady = 20)


trackcryptoprice()
win.mainloop()