import time
import datetime as dt
import numpy as np
import matplotlib as mat
import matplotlib.pyplot as plt
import scipy

from math import sqrt,pi
from scipy.stats import norm
from scipy.optimize import brentq
from scipy.interpolate import interp1d

from wrapper import get_eod_data, transform_dfs

puts, calls = get_eod_data()
df_puts, df_calls = transform_dfs(puts, calls)
print(df_calls)


def N(z):
    return norm.cdf(z)

def black_scholes_call_val(S,K,r,t,vol): 
    d1 = (1.0 /(vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t) 
    d2 = d1 - (vol * np.sqrt(t))
    return N(d1) * S - N(d2) * K * np.exp(-r * t)

def black_scholes_put_val(S,K,r,t,vol): 
    d1 = (1.0 /(vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t) 
    d2 = d1 - (vol * np.sqrt(t))
    return N(-d2) * K * np.exp(-r * t) - N(-d1) * S

def get_days_until_exp(series):
    exp = series["expirationDate"]
    date_str = exp.strftime("%")