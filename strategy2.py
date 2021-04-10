import ccxt
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
candles = exchange.fetch_ohlcv('BTC/USDT',timeframe='5m',limit = 1000)
df = pd.DataFrame(candles, columns=['timestam','o','h','l','c','vol'])
rsi = RSIIndicator(df['c'])
bb = BollingerBands(df['c'])
df["ub"] ,df["lb"]  ,df["bbma"],df['rsi']  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg() ,rsi.rsi()

c = df.loc[df['rsi']<=50]
print(c)
x = c.loc[df['o']<df['lb']]
y = x.loc[df['c']>df['lb']]

print(y)



# for x in range(len(df)):
#     if df[x]['o']<df[x]['lb'] and df[x]['lb']<df[x]['c']:
#         print(x,df[x]['o'],df[x]['lb'],df[x]['c'])    