class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charMap = {}
        maxLen = 0
        for r in range(len(s)):

            charMap[s[r]] = charMap.get(s[r], 0) + 1
            while charMap[s[r]] > 1:
                charMap[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r-l+1)
        return maxLen
            


            