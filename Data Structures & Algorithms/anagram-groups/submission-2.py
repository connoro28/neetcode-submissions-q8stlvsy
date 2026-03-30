class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = defaultdict(list)
        for s in strs:
            alarr = [0]*26
            for c in s:
                alarr[ord(c)-ord("a")] += 1
            resMap[tuple(alarr)].append(s)
        return list(resMap.values())
