class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev):
            if i >= len(nums):
                return 0
            if (i, prev) in memo:
                return memo[(i, prev)]
            if nums[i] > prev:
                memo[(i,prev)] = max(dfs(i+1, prev), 1 + dfs(i+1, nums[i]))
            else:
                memo[(i, prev)] = dfs(i+1, prev)
            return memo[(i, prev)]
        res = dfs(0, float('-inf'))
        return res
            
            
            