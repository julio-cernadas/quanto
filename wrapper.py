#!/usr/bin/env/python3
import json
import requests
import pandas as pd
import requests
import numpy as np

from datetime import date, timedelta
from pandas.compat import StringIO

# TODO:
# - add 'currency','openInterest', etc eventually

"""
option price
current stock price
strike price 
risk free interest rate
t is the time to maturity
N denotes a normal distribution
"""

# Retrieving Data
key = ""
def get_eod_data(symbol = "HD.US", api_token = key):
	url  = "https://eodhistoricaldata.com/api/options/" + symbol
	data = {	"api_token" : api_token}
	dictionary = requests.get(url, params = data).json() 
	keys = list(dictionary.keys())
	data = keys[2]
	resp = dictionary[data]
	lst1 = [x for x in resp]
	lst2 = list()
	for x in lst1:
		put,call = x["options"]["PUT"], x["options"]["CALL"]
		df = pd.DataFrame.from_dict(call+put)
		lst2.append(df)
	return pd.concat(lst2)

def transform_df(data):
	df = data[["expirationDate","contractName","type","strike",
				"inTheMoney","lastPrice","change","changePercent",
				"volume","impliedVolatility","delta","gamma","theta",
				"vega","rho","theoretical","intrinsicValue","timeValue"]]
	df.set_index("expirationDate",inplace=True)
	return df

df = transform_df(get_eod_data())
print(df)