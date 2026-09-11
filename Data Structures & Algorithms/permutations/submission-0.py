class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    dfs(curr)
                    curr.pop()
        dfs([])
        return res
                