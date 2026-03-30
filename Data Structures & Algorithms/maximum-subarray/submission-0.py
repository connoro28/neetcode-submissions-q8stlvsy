class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tSum = 0
        maxSum = nums[0]
        for r in range(len(nums)):
            tSum = tSum + nums[r]
            maxSum = max(maxSum, tSum)
            if tSum < 0:
                tSum = 0
        return maxSum

