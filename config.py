import ccxt
apiKey = '0NeK1vuB1Sutzvg1qKCtGHiaoWRv85ITY1kB9DIWVHIxtWI2vXERjVkdtHs2IpNC'
apiSecret = '1uEY4qDO50cMJkWRLY5B9x6PyMB87UwXjHkfwg9CHzkAaURrvgGFcEPObHXcSpXZ'
telegramApi = '1767236078:AAEVdujL2BGDW9NB9-4XQsmSvWygCYtUtMk'

exchange = ccxt.binance(
    {
        'apiKey':apiKey,
        'secret':apiSecret,
    }
)
