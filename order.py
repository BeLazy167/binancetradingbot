# import ccxt
# import config
# exchange = config.exchange
# balance = exchange.fetch_balance()['total']['USDT']
# print(balance)
# candles = exchange.fetch_ohlcv('NMR/USDT',timeframe='5m',limit = 1)
# total = float(balance/candles[0][4])
# print(exchange.markets['NMR/BTC']['limits']['cost']['min'])
# print(total)
# print(exchange.create_market_buy_order("NMR/USDT",total))
# exchange.create_market_buy_order
# params = {
#     type: 'TAKE_PROFIT',
#     "stopPrice": 54000,
#     "symbol": 'BTCUSDT',
#     "side": 'BUY',
#     "quantity": 0.005,
#     "price": 53000,
#     "timeInForce": 'GTX'
# }

