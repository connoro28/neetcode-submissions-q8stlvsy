class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = 0
        r = len(nums) - 1
        res = []
        for c in range(len(nums)):
            l = c +1
            r = len(nums) - 1
            while l < r:
                tSum = nums[l] + nums[r] + nums[c]
                if tSum == 0:
                    if [nums[c],nums[l],nums[r]] not in res:
                        res.append([nums[c],nums[l],nums[r]])
                    l+=1
                elif tSum < 0:
                    l += 1
                else:
                    r-=1
        return res