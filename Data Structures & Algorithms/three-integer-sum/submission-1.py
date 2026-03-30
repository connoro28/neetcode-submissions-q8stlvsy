class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, n in enumerate(nums):

            currFixed = n
            if i > 0 and n == nums[i-1]:
                continue
            left = i
            right = len(nums) - 1
            while left < right:
                if i == left:
                    left +=1
                    continue
                currSum = currFixed + nums[left] + nums[right]
                if currSum > 0:
                    right -= 1
                elif currSum < 0:
                    left += 1
                else:
                    result.append([currFixed, nums[left], nums[right]])
                    left += 1
                    right -=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    continue
        return result 
            