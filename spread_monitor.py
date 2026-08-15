def calculate_spread(price_a, price_b):
    spread = ((price_b - price_a) / price_a) * 100
    return spread


price_binance = 117250
price_bybit = 117890

spread = calculate_spread(price_binance, price_bybit)

print(f"Spread: {spread:.3f}%")
