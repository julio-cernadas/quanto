#!/usr/bin/env/python3
import json
import requests
import pandas as pd
import requests
import numpy as np

from datetime import date, timedelta
from pandas.compat import StringIO

# retrieving data from EODHistoricalData.com API services
key = ""
def get_eod_data(symbol = "AAPL.US", api_token = key):
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
		"theoretical","timeValue","updatedAt","vega","impliedVolatility"]
		puts,calls = pd.DataFrame.from_dict(put), pd.DataFrame.from_dict(call)
		puts.drop(cols,axis=1,inplace=True)
		calls.drop(cols,axis=1,inplace=True)
		put_lst.append(puts)
		call_lst.append(calls)
	return pd.concat(put_lst),pd.concat(call_lst)

# transforming plain data into valuable input... remember GIGO
def transform_dfs(df_puts,df_calls):
	df_puts.reset_index(drop=True,inplace=True)
	df_calls.reset_index(drop=True,inplace=True)
	cols = ["expirationDate","type","strike","inTheMoney",
			"lastPrice","bid","ask","volume"]
	df_P,df_C = df_puts[cols], df_calls[cols]
	convert_dict = {"strike"    : float,
					"lastPrice" : float,
					"bid"		: float,
					"ask"		: float,
					"volume"    : float}
	df_P, df_C = df_P.astype(convert_dict), df_C.astype(convert_dict)
	columns = {	"expirationDate": "expDate",
				"type"			: "type",
				"strike"		: "strike",
				"inTheMoney"	: "itm",
				"lastPrice" 	: "last",
				"bid"			: "bid",
				"ask"			: "ask",
				"volume"		: "vol"}
	df_P.rename(columns=columns,inplace=True)
	df_C.rename(columns=columns,inplace=True)
	return df_P, df_C