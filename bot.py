import ccxt
import time
# from datetime import datetime

exchange = ccxt.bybit({
    'apiKey': 'r6qRbA9v9fmOIw459E',
    'secret': 'H7JTng1e0WyMzd81gbCoX16c7v47TzGyHP7L',
    'timeout': 30000,
    "enableRateLimit": True
})

exchange.set_sandbox_mode(True)  # activates testnet mode

symbol = 'BTC/USDT:USDT'
timeframe = '1m'
limit = 100
order_size = 0.1  # set the order size here

long_position = False
short_position = False


