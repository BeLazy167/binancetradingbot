import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *
RSI_PERIOD = 13
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
BB_PERIOD = 30
TRADE_SYMBOL = 'BTCUSDT'

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_5m"
closes = []
def on_open(ws):
    pass
def on_close(ws):
    pass
def on_message(ws , message):
    global closes
    jsonMessage = json.loads(message)
    pprint.pprint(jsonMessage)
    isClose = jsonMessage['k']['x'] 
    if isClose :
        closes.append(float(jsonMessage['k']['c']))
        print(closes)
        if len(closes)>BB_PERIOD:
            npCloses = numpy.array(closes)
            rsi = talib.RSI(npCloses,RSI_PERIOD)
            upperband, middleband, lowerband = talib.BBANDS(npCloses, timeperiod=30, nbdevup=2, nbdevdn=2, matype=0)



ws = websocket.WebSocketApp(SOCKET,on_open=on_open, on_close=on_close,on_message=on_message)
ws.run_forever()