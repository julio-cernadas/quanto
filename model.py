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

def phi(x):
    return np.exp(-0.5 * x * x) / (sqrt(2.0 * pi))

def call_delta(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    return N(d1)

def put_delta(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    return N(d1) - 1.0

def gamma(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    return phi(d1) / (S * vol * sqrt(t))

def vega(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    return (S * phi(d1) * sqrt(t)) / 100.0

def call_theta(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    theta = -((S * phi(d1) * vol) / (2.0 * np.sqrt(t))) - \
                (r * K * np.exp(-r * t) * N(d2))
    return theta / 365.0

def put_theta(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    theta = -((S * phi(d1) * vol) / (2.0 * np.sqrt(t))) + \
                (r * K * np.exp(-r * t) * N(-d2))
    return theta / 365.0

def call_rho(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    rho = K * t * np.exp(-r * t) * N(d2)
    return rho / 100.0

def put_rho(S,K,r,t,vol):
    d1 = (1.0 / (vol * np.sqrt(t))) * (np.log(S / K) + (r + 0.5 * vol**2.0) * t)
    d2 = d1 - (vol * np.sqrt(t))
    rho = -K * t * np.exp(-r * t) * N(-d2)
    return rho / 100.0

# def call_implied_volatility_obj_func(S,K,r,t,vol,call_price):
#     return call_price - black_scholes_call_val(S,K,r,t,vol)

def get_days_until_exp(df):
    exp = df["expDate"]
    date_str = exp + " 23:59:59"
    expiry = dt.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
    today  = dt.datetime.today()
    return (expiry - today).days + 1

def get_time_fraction_until_exp(df):
    exp = df["expDate"]
    date_str = exp + " 23:59:59"
    time_tuple = time.strptime(date_str,"%Y-%m-%d %H:%M:%S")
    expiry_in_seconds_from_epoch = time.mktime(time_tuple)
    right_now_in_seconds_from_epoch = time.time()
    seconds_until_expiration = expiry_in_seconds_from_epoch - \
    right_now_in_seconds_from_epoch
    seconds_in_year = 31536000.0
    return max(seconds_until_expiration / seconds_in_year, 1e-10)

terms = [30, 30*3, 30*6, 30*12, 30*24, 30*36, 30*60]
rates = [0.0001, 0.0009, 0.0032, 0.0067, 0.0097, 0.0144, 0.0184]

def get_rate(df):
    days = df["DaysUntilExp"]
    new_terms = [i for i in range(30,(60 * 30) + 1)]
    f = interp1d(terms, rates, kind="linear")
    ff = f(new_terms)
    return round(ff[max(days,30) - 30], 8)

def get_mid(df):
    bid = df["bid"]
    ask = df["ask"]
    last = df["last"]
    if np.isnan(ask) or np.isnan(bid):
        return 0.0
    elif ask == 0.0 or bid == 0.0:
        return last
    else:
        return (ask + bid) / 2.0

df_calls["DaysUntilExp"] = df_calls.apply(get_days_until_exp, axis=1)
df_calls["TimeUntilExp"] = df_calls.apply(get_time_fraction_until_exp, axis=1)
df_calls["InterestRate"] = df_calls.apply(get_rate, axis=1)
df_calls["Mid"] = df_calls.apply(get_mid, axis=1)

print(df_calls.head(50))

