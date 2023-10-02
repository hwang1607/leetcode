class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] < prices[r]:
                curr = prices[r] - prices[l]
                maxp = max(maxp, curr)
            else:
                l = r
            r += 1

        return maxp

        
                
        
        
        