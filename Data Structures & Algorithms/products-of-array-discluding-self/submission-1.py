class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tSum = 1
        arr2 = [1] * len(nums)
        res = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            arr2[i] = tSum
            tSum *= nums[i]
        
        arr1 = []
        tSum = 1
        for i, n in enumerate(nums):
            arr1.append(tSum * arr2[i])
            tSum *= n
        return arr1


