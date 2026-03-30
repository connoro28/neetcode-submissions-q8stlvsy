class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        currSum = 0
        maxProf = 0
        for r in range(len(prices)):
            currSum = prices[r] - prices[l]
            maxProf = max(maxProf, currSum)
            if prices[r] < prices[l]:
                l = r
        return maxProf
            