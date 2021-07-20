import ccxt ,time , pprint
import pandas as pd
from ta.trend import EMAIndicator
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
#import error---------------------
# import config
# exchange = config.exchange

#after we solve error in import we can remove this
apiKey = 'e57nLX70nvRUghUFvQrSDkXnHw7CBAX4lJl0npLYpR7YqxP8sRYitbTvdKFjfxgF'
apiSecret = 'PqGJQ4Tu6fWSqxEvlPsS88tfcPoV3q1iyS0tuRKFddHFQXwKYmvC1dniwQdJdBe6'
exchange = ccxt.binance(
    {
        'apiKey':apiKey,
        'secret':apiSecret,
    }
)
####################


symbol = "BTC/USDT"
def tradefinder(symbol):
    while True:
        candles = exchange.fetch_ohlcv(symbol,timeframe='1h',limit = 5000)
        df = pd.DataFrame(candles[:201], columns=['timestam','o','h','l','c','vol'])
        ema1 = EMAIndicator(df['c'],window = 200)
        ema2 = EMAIndicator(df['c'],window = 50)
        rsi = RSIIndicator(df['c'])
        bb = BollingerBands(df['c'])
        df["ub"] ,df["lb"]  ,df["bbma"],df['rsi'],df['200EMA'],df['50EMA']  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg() ,rsi.rsi() ,ema1.ema_indicator(),ema2.ema_indicator()
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
            time.sleep(10)

tradefinder(symbol)
