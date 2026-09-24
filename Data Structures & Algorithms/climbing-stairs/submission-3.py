class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dfs(state):
            if state <=2:
                return state
            if state in memo:
                return memo[state]
            memo[state] = dfs(state-1) + dfs(state-2)
            return memo[state]
        return dfs(n)