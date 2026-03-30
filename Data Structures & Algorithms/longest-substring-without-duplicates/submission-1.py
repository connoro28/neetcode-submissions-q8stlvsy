class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curr = ""
        maxS = 0
        currS = 0
        while r <= len(s)-1:
            if s[r] not in curr:
                curr += s[r]
                r += 1
            else:
                l += 1
                curr = curr[1:]
            currS = len(curr)
            maxS = max(currS, maxS)
        return maxS
