class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        sumt = 0
        res = len(nums) + 1
        for r in range(len(nums)):
            sumt += nums[r]
            while sumt >= target:
                res = min(res, r-l+1)
                sumt -= nums[l]
                l+=1
        if res == len(nums) + 1:
            return 0
        return res
