class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for n in nums:
            if n in numMap:
                return True
            else:
                numMap[n] = 1
        return False