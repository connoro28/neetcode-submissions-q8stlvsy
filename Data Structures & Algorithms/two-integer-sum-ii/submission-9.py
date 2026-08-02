class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            targ = numbers[l] + numbers[r]
            if targ == target:
                return [l+1, r+1]
            if targ > target:
                r-=1
                continue
            if targ < target:
                l +=1
                continue
            