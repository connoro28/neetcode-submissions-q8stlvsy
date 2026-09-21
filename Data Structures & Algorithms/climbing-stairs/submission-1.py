class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(state):
            if state <= 2:
                return state
            if state in memo:
                return memo[state]
            memo[state] = dp(state-1) + dp(state-2)
            return memo[state]
        return dp(n)