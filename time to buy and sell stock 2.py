class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = 0
        b = 0
    
        for i in range(len(prices)-1):
            a = prices[i+1] - prices[i]
            if a > 0:
                b += a
            elif a < 0:
                a = 0
        return b
