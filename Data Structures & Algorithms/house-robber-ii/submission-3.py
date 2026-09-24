class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def robline(arr):
            memo = {}
            def dfs(i):
                if i >= len(arr):
                    return 0
                if i in memo:
                    return memo[i]
                memo[i] = max(arr[i]+dfs(i+2), dfs(i+1))
                return memo[i]
            return dfs(0)
        return max(robline(nums[1:]), robline(nums[:-1]))