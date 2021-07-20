import ccxt ,time , pprint
from datetime import datetime 
import pandas as pd
from ta.volatility import BollingerBands
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator

apiKey = '0NeK1vuB1Sutzvg1qKCtGHiaoWRv85ITY1kB9DIWVHIxtWI2vXERjVkdtHs2IpNC'
apiSecret = '1uEY4qDO50cMJkWRLY5B9x6PyMB87UwXjHkfwg9CHzkAaURrvgGFcEPObHXcSpXZ'
telegramApi = '1767236078:AAEVdujL2BGDW9NB9-4XQsmSvWygCYtUtMk'

exchange = ccxt.binance(
    {
        'apiKey':apiKey,
        'secret':apiSecret,
    }
)

def dataf(sym):
    candles = exchange.fetch_ohlcv(sym,timeframe='1h', limit = 1000)
    df = pd.DataFrame(candles, columns=['timestam','o','h','l','c','vol'])
    print(df.size//6)
    return df

def dgcross(sym): #death/golden cross
    df = dataf(sym)
    ema1 = EMAIndicator(df['c'],window = 200)
    ema2 = EMAIndicator(df['c'],window = 50)
    df['ema200'],df['ema50'] ,df['sub'], df['date']= ema1.ema_indicator(),ema2.ema_indicator(),ema1.ema_indicator()-ema2.ema_indicator(),pd.to_datetime(df['timestam'],unit='ms')
    #to find the cross we subract the values and find if the values are close to 0
    x= df.loc[df['sub']<10]
    y= x.loc[-10<df['sub']]
    data = pd.DataFrame(y)
    data.to_excel("output.xlsx")
    return 0 

def bbRsi(sym):

    df  = dataf(sym)
    rsi = RSIIndicator(df['c'])
    bb = BollingerBands(df['c'])
    df["ub"] ,df["lb"]  ,df["bbma"],df['rsi'],df['timestam']  = bb.bollinger_hband() , bb.bollinger_lband(), bb.bollinger_mavg() ,rsi.rsi(), pd.to_datetime(df['timestam'],unit='ms')
    c = df.loc[df['rsi']<40]
    x = c.loc[df['o']<df['lb']]
    y = x.loc[df['c']>df['lb']]
    print(sym)
    print(y)
    signal = y.size//11
    print(signal)
    return signal
totalSignal = 0
syms = ['BTC/USDT','ETH/USDT','XRP/USDT','LTC/USDT','BCH/USDT','TRX/USDT',"EOS/USDT",'LINK/USDT',"BNB/USDT"]
for sym in syms:
    signals = dgcross(sym)
    totalSignal = signals + totalSignal
    break
print(totalSignal)