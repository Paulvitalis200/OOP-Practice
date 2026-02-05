# Write code to return top traded stocks given a list of stocks

# APPL: 300
# GOOGL: 499
# BLOOM: 900

# Methodology
# Keep track of number of trades on each stock. Key value. Probably a hashmap/dictionary
# When a trade is made, increment the count in the hashmap
# Order the hashmap
# Add method to return top(n) stocks

class Stocks:
    def __init__(self):
        self.stocks = {}

    def record_trade(self, stock_name, amount):
        if stock_name not in self.stocks:
            self.stocks[stock_name] = amount
        else:
            self.stocks[stock_name] += amount

    def print_top_stocks(self, n):
        ordered_stocks = sorted(self.stocks.items(), key=lambda x: x[1], reverse=True)

        return ordered_stocks[:n]


stocks = Stocks()
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
stocks.record_trade('Netflix', 600)
stocks.record_trade('Microsoft', 200)
stocks.record_trade('Netflix', 1000)
stocks.record_trade('Netflix', 300)
print(stocks.print_top_stocks(3))