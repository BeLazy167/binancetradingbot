import ccxt ,time , pprint
import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
import config

exchange = config.exchange
symbol = "BTC/USDT"
def tradefinder(symbol):
    while True:
        candles = exchange.fetch_ohlcv(symbol,timeframe='5m',limit = 21)
        df = pd.DataFrame(candles[:20], columns=['timestam','o','h','l','c','vol'])
        rsi = RSIIndicator(df['c'])
        bb = BollingerBands(df['c'])
        df["ub"] ,df["lb"]  ,df["bbma"],df['rsi']  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg() ,rsi.rsi()
        finalData = df.tail(1).values.tolist()[0]
        pprint.pprint(df)
        if finalData[9]<40 and finalData[1]<finalData[7] and finalData[7]<finalData[4]:
            print('enter')
            continue
        else:
            print('not yet')
            epoch = (finalData[0]//1000)+600
        
        while time.time() <= epoch:
            print(epoch)
            print(int(time.time()))
            time.sleep(1)

tradefinder(symbol)
