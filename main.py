import config as cf

#import from config
config = cf.config()
client = config.login()
info = client.get_account()
balance = client.get_asset_balance(asset='usdt')

print(balance)
