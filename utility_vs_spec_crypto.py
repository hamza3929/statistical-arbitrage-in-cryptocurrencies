# 1. research question:
# do crypto with utility functions perform better compared to coins that are more speculative or trendy?

# 2. hypothesis:
# crypto with utility functions will perform better than coins that are more speculative or trendy

# 3. define asset groups
# group 1: utility coins (e.g. Ethereum, Binance Coin, Cardano)
# group 2: speculative coins (e.g. Dogecoin, Shiba Inu, SafeMoon)

# 4. data collection
# collect historical price data for the selected coins in both groups over a specific time period (e.g. 1 year)

from binance.client import Client as bnb_client
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

client = bnb_client()

def getbinancedata(symbol, freq, start_str, end_str):
    klines = client.get_historical_klines(symbol, freq, start_str, end_str)
    df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df = df.astype(float)
    return df

def returns(df):
    return df['close'].pct_change().dropna()

def sharpe_ratio(returns, risk_free_rate=0):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)

def volatility(returns):
    return np.std(returns)

def dropdown(returns):
    cumulative_returns = (1 + returns).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown.min()

def correlation(returns1, returns2):
    return returns1.corr(returns2)
#========================================================================================================================================
#                                                           Visualization

#========================================================================================================================================