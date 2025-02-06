def max_profit(prices) -> int:
    profit = 0
    min_val = float(inf)
    for price in prices:
        if price < min_val:
            min_val = price
            profit = max(profit, price - min_val)

    return profit