import ccxt
apiKey = 'e57nLX70nvRUghUFvQrSDkXnHw7CBAX4lJl0npLYpR7YqxP8sRYitbTvdKFjfxgF'
apiSecret = 'PqGJQ4Tu6fWSqxEvlPsS88tfcPoV3q1iyS0tuRKFddHFQXwKYmvC1dniwQdJdBe6'
telegramApi = '1767236078:AAEVdujL2BGDW9NB9-4XQsmSvWygCYtUtMk'

exchange = ccxt.binance(
    {
        'apiKey':apiKey,
        'secret':apiSecret,
    }
)