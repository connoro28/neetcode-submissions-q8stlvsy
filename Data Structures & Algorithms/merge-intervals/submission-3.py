class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i in intervals:
            if res:
                if i[0] <= res[-1][-1]:
                    res[-1] = [min(i[0], res[-1][0]), max(i[-1], res[-1][-1])]
                else:
                    res.append(i)
            else:
                res.append(i)
        return res