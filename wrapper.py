#!/usr/bin/env/ python3
import json
import requests
import pandas as pd
from datetime import date, timedelta
# TODO: 
def get_last_price(ticker):
	url = "https://www.alphavantage.co/query"
	function = "TIME_SERIES_DAILY_ADJUSTED"
	symbol = ticker
	outputsize= "compact"
	api_key = "4I16NYFU17Q3KNKC"
	data = { "function": function,
			"symbol": symbol,
			"outputsize": outputsize,
			"apikey": api_key }
	try: 
		dictionary = requests.get(url, params = data).json() 
		keys = list(dictionary.keys())
		series = keys[1]
		resp  = dictionary[series]
		dict_ = next(iter(resp.values()))
		pricing = {	"Symbol": ticker,
					"Open"  : float(dict_['1. open']),
					"High"  : float(dict_['2. high']),
					"Low"   : float(dict_['3. low']),
					"Close" : float(dict_['4. close']),
					"Vol"   : float(dict_['5. volume']) }
		return pricing
	except:
		return None

def get_prices_df(ticker):
    url = "https://www.alphavantage.co/query"
    function = "TIME_SERIES_DAILY_ADJUSTED"
    symbol = ticker
    outputsize= "compact"
    api_key = "4I16NYFU17Q3KNKC"
    data = { "function": function,
            "symbol": symbol,
            "outputsize": outputsize,
            "apikey": api_key }
    try:
        dictionary = requests.get(url, params = data).json() 
        keys = list(dictionary.keys())
        series = keys[1]
        resp = dictionary[series]
        df = pd.DataFrame.from_dict(resp, orient='index')
        df['date'] = pd.to_datetime(df.index)
        fivemonthsago = date.today() - timedelta(140)
        df = df.rename(columns={"5. adjusted close": "Price"})
        df = df[(df['date']>=fivemonthsago)][['Price','date']].set_index('date')
        return df
    except:
        return None

print(get_prices_df("HD"))

def get_company_name(ticker):
	try:
		endpoint = 'http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol='+ticker
		response = requests.get(endpoint).json()
		company_name = response['Name']
		return company_name
	except:
		return 'N/A'
