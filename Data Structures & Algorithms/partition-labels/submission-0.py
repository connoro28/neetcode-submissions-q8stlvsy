class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervalMap = {}
        result = []
        for i, c in enumerate(s):
            if c in intervalMap:
                intervalMap[c].append(i)
            else:
                intervalMap[c] = [i]
        intervalarr = []
        for ints in intervalMap.values():
            intervalarr.append([ints[0], ints[-1]])
        res = []
        for ints in intervalarr:
            if res:
                if ints[0] <= res[-1][-1]:
                    res[-1] = [min(ints[0], res[-1][0]), max(ints[-1], res[-1][-1])]
                else:
                    res.append(ints)
            else:
                res.append(ints)
        for i in res:
            diff = i[-1] - i[0] + 1
            result.append(diff)
        return result
