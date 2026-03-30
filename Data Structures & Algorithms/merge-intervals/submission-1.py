class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in intervals:
            if res and i[0] <= res[-1][-1]:
                if res[-1][-1] > i[-1]:
                    continue
                else:
                    res[-1][-1] = i[-1]
            else:
                res.append(i)
        return res