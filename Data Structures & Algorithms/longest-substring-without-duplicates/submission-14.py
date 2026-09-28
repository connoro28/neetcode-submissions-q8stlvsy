class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        activechars = set()
        l = 0
        for r in range(len(s)):
            while s[r] in activechars:
                activechars.remove(s[l])
                l+=1
            activechars.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen
