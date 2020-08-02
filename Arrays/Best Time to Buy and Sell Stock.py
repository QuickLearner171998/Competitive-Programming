class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0 or len(prices)== 1:
            return 0
        mp = 0
        cp = prices[0]
        for i, price in enumerate(prices):
            if price < cp:
                cp = price
            else:
                mp =max(mp, price - cp)
        return mp
