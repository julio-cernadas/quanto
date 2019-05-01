#!/usr/bin/env/python3
import json
import requests
import pandas as pd
import requests
import numpy as np

from datetime import date, timedelta
from pandas.compat import StringIO

# retrieving current price/spot data from Alpha Vantage API
def get_last_price(ticker):
	url = "https://www.alphavantage.co/query"
	function = "TIME_SERIES_INTRADAY"
	symbol = ticker
	interval = "1min"
	outputsize= "compact"
	api_key = "4I16NYFU17Q3KNKC"
	data = { "function": function,
			"symbol": symbol,
			"interval": interval,
			"outputsize": outputsize,
			"apikey": api_key }

	try:
		dictionary = requests.get(url, params = data).json() 
		keys = list(dictionary.keys())
		series = keys[1]
		resp = dictionary[series]
		dict_ = next(iter(resp.values()))
		last_price = dict_['1. open']
		return float(last_price)
	except:
		return 0.0

# retrieving data from EODHistoricalData.com API services
key = "5c958084138e54.81660498"
def get_eod_data(symbol, api_token = key):
	stock_price = get_last_price(symbol.replace(".US",""))
	url  = "https://eodhistoricaldata.com/api/options/" + symbol
	data = {	"api_token" : api_token}
	dictionary = requests.get(url, params = data).json() 
	keys = list(dictionary.keys())
	data = keys[2]
	resp = dictionary[data]
	lst1 = [x for x in resp]
	put_lst, call_lst = list(), list()
	for x in lst1:
		put,call = x["options"]["PUT"], x["options"]["CALL"]
		cols = ["change","changePercent","contractName","contractSize","currency",
		"delta","lastTradeDateTime","rho","theta","gamma","intrinsicValue",
		"theoretical","timeValue","updatedAt","vega"]
		puts,calls = pd.DataFrame.from_dict(put), pd.DataFrame.from_dict(call)
		puts.drop(cols,axis=1,inplace=True)
		calls.drop(cols,axis=1,inplace=True)
		puts["spot"]  = float(stock_price)
		calls["spot"] = float(stock_price)
		put_lst.append(puts)
		call_lst.append(calls)
	return pd.concat(put_lst),pd.concat(call_lst)

# transforming plain data into valuable output... remember GIGO
def transform_dfs(df_puts,df_calls):
	df_puts.reset_index(drop=True,inplace=True)
	df_calls.reset_index(drop=True,inplace=True)
	cols = ["expirationDate","type","strike","spot","inTheMoney",
			"lastPrice","bid","ask","volume","impliedVolatility"]
	df_P,df_C = df_puts[cols], df_calls[cols]
	convert_dict = {"strike"    : float,
					"spot"		: float,
					"lastPrice" : float,
					"bid"		: float,
					"ask"		: float,
					"volume"    : float}
	df_P, df_C = df_P.astype(convert_dict), df_C.astype(convert_dict)
	columns = {	"expirationDate": "expDate",
				"type"			: "type",
				"strike"		: "strike",
				"spot"			: "spot",
				"inTheMoney"	: "ITM",
				"lastPrice" 	: "price",
				"bid"			: "bid",
				"ask"			: "ask",
				"volume"		: "volume",
				"impliedVolatility"	: "IV"}
	df_P.rename(columns=columns,inplace=True)
	df_C.rename(columns=columns,inplace=True)
	return df_P, df_C

