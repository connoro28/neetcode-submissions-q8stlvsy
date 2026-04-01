class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        idMap = defaultdict(list)
        for s in strs:
            idArr = [0] * 26
            for c in s:
                idArr[ord(c)-ord("a")] += 1
            idMap[tuple(idArr)].append(s)
        return list(idMap.values())
            
