class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tsum = 0
        maxSum = nums[0]
        for n in nums:
            tsum += n
            maxSum = max(maxSum, tsum)
            if tsum < 0:
                tsum = 0
        return maxSum