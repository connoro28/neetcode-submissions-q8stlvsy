class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for c in range(len(nums)-2):
            if c > 0 and nums[c] == nums[c-1]:
                continue
            l = c + 1
            r = len(nums) - 1
            while l < r:
                currSum = nums[c] + nums[l] + nums[r]                
                if currSum == 0:
                    res.append([nums[c], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l+=1
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l += 1
                    r -= 1
                elif currSum < 0:
                    l+=1
                else:
                    r-=1
        return res

