









## product prices ##
class ProductPrice:
    def __init__(self) -> None:
        self.prices = []
        self.min = float('inf')
        self.max = float('-inf')

    def update(self, ts, price):
        self.prices.append((ts, price))
        if price < self.min:
            self.min = price
        if price > self.max:
            self.max = price

    def minimum(self):
        if not self.prices:
            return None
        return self.min

    def maximum(self):
        if not self.prices:
            return None
        return self.max

    def lastest(self):
        if not self.prices:
            return None
        return self.prices[-1][-1]