class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idMap = defaultdict(list)
        res = []
        for s in strs:
            arr = [0] * 26
            for c in s:
                i = ord(c) - ord("a")
                arr[i] += 1
            if tuple(arr) in idMap:
                idMap[tuple(arr)].append(s)
            else:
                idMap[tuple(arr)] = [s]
        for a in idMap.values():
            res.append(a)
        return res