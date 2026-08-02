class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cMap = {}
        l = 0
        best = 0
        for r in range(len(s)):
            if s[r] in cMap and cMap[s[r]] >= l:
                l = cMap[s[r]] + 1
            cMap[s[r]] = r
            best = max(best, r-l +1)
        return best


            