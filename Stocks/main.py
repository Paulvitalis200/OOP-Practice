# Write code to return top traded stocks
# Record each trade as key and value pair
# When a trade is made, increment/decrement the value of that key
# Sort the hashmap and return the top 3 items in the hashmap

class Stocks:
    def __init__(self):
        self.hash_map = {}

    def record_trade(self, stock, value):
        # {'Netflix': 500}
        if stock in self.hash_map:
            self.hash_map[stock] = self.hash_map[stock] + value
        else:
            self.hash_map[stock] = value

    def print_top_stocks(self, n):
        sorted_stocks = dict(sorted(self.hash_map.items(), key=lambda x:x[1], reverse=True))

        count = 0
        for key, value in sorted_stocks.items():
            if count < n:
                print(key + ' | ' + str(value))
                count += 1
       


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
print(stocks.print_top_stocks(5))