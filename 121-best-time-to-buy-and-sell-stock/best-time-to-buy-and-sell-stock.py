class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        n = len(prices)
        for price in prices:
            if price > min_price:
                max_profit =max(max_profit, price - min_price)
            if price < min_price:
               min_price = price
        return max_profit
        