class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for n in nums:
            numDict[n] = numDict.get(n, 0) + 1
        res = []
        for i in range(k):
            maxkey = max(numDict, key=numDict.get)
            res.append(maxkey)
            del numDict[maxkey]
        return res