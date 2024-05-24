#Getting Notcoin Real time price Using PyCoinGecko for CoinGecko API:
from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()

#Get notcoin data 
notcoin_data = cg.get_coin_market_chart_by_id(id = 'notcoin', vs_currency = 'ngn', days = 30)
#print(notcoin_data['prices'])

data = pd.DataFrame(notcoin_data['prices'], columns = ['TimeStamp', 'Prices'])

#Coverting the TimeStamp to a more readable format
data['Date'] = pd.to_datetime(data['TimeStamp'], unit = 'ms')

data.to_csv("./Notcoin_Price_Tracker.csv")