class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i-1] == a:
                continue
            l = i+1
            r = len(nums) - 1
            while l < r:
                tot = a + nums[l] + nums[r]
                if tot == 0:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif tot < 0:
                    l = l + 1
                else:
                    r = r - 1
        return res
                