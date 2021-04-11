import ccxt ,time , pprint
from datetime import datetime 
import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
import config

exchange = ccxt.binance(
    {
        'apiKey':config.apiKey,
        'secret':config.apiSecret,
    }
)
syms = ['BTC/USDT','ETH/USDT','XRP/USDT']
for sym in syms:
        candles = exchange.fetch_ohlcv(sym,timeframe='5m',limit = 200)
        df = pd.DataFrame(candles, columns=['timestam','o','h','l','c','vol'])
        rsi = RSIIndicator(df['c'])
        bb = BollingerBands(df['c'])
        df["ub"] ,df["lb"]  ,df["bbma"],df['rsi']  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg() ,rsi.rsi()
        c = df.loc[df['rsi']<40]
        x = c.loc[df['o']<df['lb']]
        y = x.loc[df['c']>df['lb']]
        print(sym)
        print(y)