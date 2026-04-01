class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        count = 0
        l = 0
        for r in range(len(s)):
            if s[r] in charMap:
                while s[r] in charMap:
                    del charMap[s[l]]
                    l+=1
                count = max(count, r-l+1)
            else:
                count = max(count, r-l+1)
            charMap[s[r]] = 1
        return count
