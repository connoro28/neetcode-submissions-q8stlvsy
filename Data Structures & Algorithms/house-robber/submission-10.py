class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        self.maxValue = 0
        def dp(i):
            if i < 0:
                return 0
            if i <= 1:
                self.maxValue = max(self.maxValue, nums[i])
                return nums[i]
            if i in memo:
                self.maxValue = max(self.maxValue, memo[i])
                return memo[i]
            memo[i] = nums[i] + max(dp(i-2), dp(i-3))
            self.maxValue = max(memo[i], self.maxValue)
            return memo[i]
        for n in range(len(nums)):
            dp(n)
        return self.maxValue