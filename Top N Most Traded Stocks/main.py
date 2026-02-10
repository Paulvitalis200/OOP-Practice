# Problem
# Instead of summing trade amounts, return the top N stocks by number of trades.

# Follow-up

# How would you support both total volume and trade count?

# Time complexity?
# AAPL: 400
# META: 500
# AAPL: 500

class StockStat:
    def __init__(self):
        self.volume = 0
        self.count = 0

class Trades:
    def __init__(self):
        self.hash_map = {}

    def record_trade(self, trade, amount):
        if trade not in self.hash_map:
            self.hash_map[trade] = StockStat()

        stat = self.hash_map[trade]
        stat.volume += amount
        stat.count += 1

    # def top_n_by_trades(self, n):
    def top_n_by_trades(self, n):
        sorted_trades = sorted(self.hash_map.items(), key=lambda x: -x[1].count)

        return [(trade, count.count) for trade, count in sorted_trades[:n]]


stocks = Trades()
stocks.record_trade('Netflix', 500)
stocks.record_trade('Microsoft', 1500)
stocks.record_trade('Netflix', 1000)
stocks.record_trade('Netflix', 2000)
stocks.record_trade('Bloomberg', 2000)
stocks.record_trade('Netflix', 500)
stocks.record_trade('Apple', 1500)
stocks.record_trade('Google', 1000)
stocks.record_trade('Amazon', 2000)
stocks.record_trade('Meta', 2000)
stocks.record_trade('Netflix', 500)
stocks.record_trade('Microsoft', 700)
stocks.record_trade('Netflix', 600)
stocks.record_trade('Netflix', 500)
stocks.record_trade('Bloomberg', 400)
stocks.record_trade('Netflix', 550)
stocks.record_trade('Apple', 750)
stocks.record_trade('Google', 200)
stocks.record_trade('Amazon', 1000)
stocks.record_trade('Meta', 100)
stocks.record_trade('Google', 490)
stocks.record_trade('Amazon', 840)
stocks.record_trade('Meta', 500)

print(stocks.top_n_by_trades(3))