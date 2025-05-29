from sortedcontainers import SortedSet
class StockPrice:
    def __init__(self):
        self.timestamp_prices = SortedDict()
    
    def update(self, timestamp: int, price: int) -> None:
        self.timestamp_prices[timestamp] = price

    def current(self) -> int:
        current_time, price = self.timestamp_prices.peekitem(-1)
        return price
    
    def maximum(self) -> int:
        max_price = 0
        for x in self.timestamp_prices.keys():
            if x > max_price:
                max_price = x
        return max_price
    
    def minimum(self) -> int:
        min_price = float(inf)
        for x in self.timestamp_prices.values():
            if x < min_price:
                min_price = x
        return min_price