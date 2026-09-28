class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for l, r in intervals:
            if res:
                if l <= res[-1][-1]:
                    res[-1][-1] = max(res[-1][-1], r)
                    continue
            res.append([l,r])
        return res