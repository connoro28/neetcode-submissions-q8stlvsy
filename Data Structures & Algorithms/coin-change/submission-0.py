class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt < 0:
                return float('inf')
            if amt in memo:
                return memo[amt]
            best = float('inf')
            for c in coins:
                best = min(best, 1 + dfs(amt-c))
            memo[amt] = best
            return memo[amt]
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res
            
