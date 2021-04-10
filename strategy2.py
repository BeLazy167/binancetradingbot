import ccxt
import pandas as pd
from ta.volatility import BollingerBands
import config

exchange = ccxt.binance(
    {
        'apiKey':config.apiKey,
        'secret':config.apiSecret,
    }
)
candles = exchange.fetch_ohlcv('BTC/USDT',limit = 50)
df = pd.DataFrame(candles, columns=['timestam','o','h','l','c','vol'])
bb = BollingerBands(df['c'])
print(bb)
df["ub"] ,df["lb"]  ,df["bbma"]  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg()
print(df[12]['o'])
# for x in range(len(df)):
#     if df[x]['o']<df[x]['lb'] and df[x]['lb']<df[x]['c']:
#         print(x,df[x]['o'],df[x]['lb'],df[x]['c'])    