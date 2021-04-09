import websocket, json, pprint, talib, numpy
import config
from binance.client import Client
from binance.enums import *

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_5m"

def on_open(ws):
    pass
def on_close(ws):
    pass
def on_message(ws , message):
    pass


ws = websocket.WebSocketApp(SOCKET,on_open=on_open, on_close=on_close,on_message=on_message)
ws.run_forever()