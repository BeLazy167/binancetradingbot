import ccxt
apiKey = 'api key here'
apiSecret = 'api secret here'
telegramApi = 'telegram api here'

exchange = ccxt.binance(
    {
        'apiKey':apiKey,
        'secret':apiSecret,
    }
)
