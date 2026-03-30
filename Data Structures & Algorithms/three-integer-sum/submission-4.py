class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        target = 0
        for m in range(len(nums)-1):
            l = m + 1
            r = len(nums)-1
            while l < r:
                tSum = nums[m] + nums[l] + nums[r]
                if tSum > target:
                    r-=1
                elif tSum < target:
                    l+=1
                else:
                    if [nums[m], nums[l], nums[r]] not in res:
                        res.append([nums[m], nums[l], nums[r]])
                    l+=1
                    r-=1
        return res

