def calculate_spread(price_a, price_b):
    spread = ((price_b - price_a) / price_a) * 100
    return spread


price_binance = 117250
price_bybit = 117890

spread_binance_to_bybit = calculate_spread(price_binance, price_bybit)
spread_bybit_to_binance = calculate_spread(price_bybit, price_binance)

print(f"Binance → Bybit: {spread_binance_to_bybit:.3f}%")
print(f"Bybit → Binance: {spread_bybit_to_binance:.3f}%")