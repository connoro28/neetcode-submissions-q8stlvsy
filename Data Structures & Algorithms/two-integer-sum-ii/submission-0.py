class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}
        for i, n in enumerate(numbers):
            numDict.setdefault(n, i)
            targVal = target - n
            if targVal in numDict and targVal != n:
                if numDict[targVal] < i:
                    return [numDict[targVal]+1, i+1]
            


