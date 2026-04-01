class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        for n in nums:
            if n in dupMap:
                return True
            else:
                dupMap[n] = 1
        return False