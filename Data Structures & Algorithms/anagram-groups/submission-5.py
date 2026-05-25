class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #id map is the key and the value is a list of the strings
        groupMap = defaultdict(list)
        for s in strs:
            idMap = [0] * 26
            for c in s:
                i = ord(c) - ord("a")
                idMap[i] += 1
            groupMap[tuple(idMap)].append(s)
        res = []
        for value in groupMap.values():
            res.append(value)
        return res
