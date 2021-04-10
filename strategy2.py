import ccxt ,time
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
def tradefinder():
    while True:
        candles = exchange.fetch_ohlcv('BTC/USDT',timeframe='5m',limit = 21)
        df = pd.DataFrame(candles[:20], columns=['timestam','o','h','l','c','vol'])
        rsi = RSIIndicator(df['c'])
        bb = BollingerBands(df['c'])
        df["ub"] ,df["lb"]  ,df["bbma"],df['rsi']  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg() ,rsi.rsi()
        finalData = df.tail(1).values.tolist()[0]
        print(df)
        if finalData[9]<40 and finalData[1]<df[7] and df[7]<df[4]:
            print('enter')
            break
        else:
            print('not yet')
        epoch = (finalData[0]//1000)+300
        print(epoch)
        print(time.time())
        time.sleep( 50 )
# c = df.loc[df['rsi']<=50]
# x = c.loc[df['o']<df['lb']]
# y = x.loc[df['c']>df['lb']]
tradefinder()
# print(y)



# for x in range(len(df)):
#     if df[x]['o']<df[x]['lb'] and df[x]['lb']<df[x]['c']:
#         print(x,df[x]['o'],df[x]['lb'],df[x]['c'])    