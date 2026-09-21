class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def ways(i):
            if i <= 2:
                return i
            if i in memo:
                return memo[i]
            memo[i] = ways(i-1) + ways(i-2)
            return memo[i]
        return ways(n)