class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i, n in enumerate(nums):
            if (target - n) in myMap:
                return [myMap[target - n], i]
            myMap[n] = i
        return

