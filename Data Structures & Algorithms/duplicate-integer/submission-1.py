class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for n in nums:
            if n in myMap:
                return True
            else:
                myMap[n] = 0
        return False