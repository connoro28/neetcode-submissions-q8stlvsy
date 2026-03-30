class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for c in range(len(nums)):
            l = c + 1
            r = len(nums) - 1
            while l < r:
                tsum = nums[c] + nums[l] + nums[r]
                if tsum > 0:
                    r-=1
                elif tsum < 0:
                    l+=1
                else:
                    if [nums[c], nums[l], nums[r]] not in res:
                        res.append([nums[c], nums[l], nums[r]])
                    l+=1
        return res
                