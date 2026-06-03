class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff > 0:
                res = max(res, diff)
            else:
                l = r
            
            r += 1

        return res