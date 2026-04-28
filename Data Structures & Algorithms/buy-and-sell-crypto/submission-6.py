class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0

        buy = 0
        sell = 1
        mp = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                mp = max(mp, profit)
            else:
                buy = sell
            sell += 1

        return mp