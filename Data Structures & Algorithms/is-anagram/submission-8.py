class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tMap = {}
        sMap = {}
        for i in range(len(s)):
            if s[i] in sMap:
                sMap[s[i]] = sMap[s[i]] + 1
            else:
                sMap[s[i]] = 1

        for i in range(len(t)):        
            if t[i] in tMap:
                tMap[t[i]] = tMap[t[i]] + 1
            else:
                tMap[t[i]] = 1

        if (sMap == tMap):
            return True
        else:
            return False