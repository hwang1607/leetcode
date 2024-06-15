class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0

        for i in range(len(prices)):
            if prices[i] > prices[l]:
                res = max(res, prices[i] - prices[l])
            else:
                l = i
        return res