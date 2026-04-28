class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = 0
        mb = 101

        for price in prices:
            mb = min(mb, price)
            profit = price - mb
            mp = max(mp, profit)
        
        return mp