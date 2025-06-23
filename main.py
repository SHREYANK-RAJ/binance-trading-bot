from binance.client import Client
from binance.enums import *
import logging

# 🛡️ Logging setup
logging.basicConfig(filename='bot.log', level=logging.INFO)

# 🔐 Fill in your API key and secret from Binance Testnet
api_key = "19c8990b356e0a7f584748abce651d991e5daaf842eb32a31fc65f4ec671563b"
api_secret = "4505b6fe0e214fecb26971fff055fb07eb4b122acbd092061a3254583015c128"

# 🤖 Connect to Binance Futures Testnet
client = Client(api_key, api_secret, testnet=True)

def place_order(symbol, side, quantity, order_type=ORDER_TYPE_MARKET):
    try:
        print(f"📤 Placing {side} order for {quantity} {symbol}")
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=order_type,
            quantity=quantity
        )
        logging.info(f"✅ Order Placed: {order}")
        print("✅ Order placed successfully!")
        print(order)
    except Exception as e:
        logging.error(f"❌ Failed: {e}")
        print("❌ Order failed:", e)

# 🧪 Test Order: Buy 0.001 BTCUSDT
place_order("BTCUSDT", SIDE_BUY, 0.001)
