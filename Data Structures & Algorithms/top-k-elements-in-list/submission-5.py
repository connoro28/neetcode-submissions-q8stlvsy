class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for p, v in freqMap.items():
            bucket[v].append(p)
        res = []
        while k > 0 and bucket:
            temp = bucket.pop()
            for i in temp:
                k-=1
                res.append(i)
                if k == 0:
                    return res
    




