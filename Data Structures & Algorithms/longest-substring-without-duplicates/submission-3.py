class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charHash = {}
        l = 0
        maxLen = 0
        for r in range(len(s)):
            #adds to hash +1 or init as 1 if not in hash
            charHash[s[r]] = charHash.get(s[r], 0) + 1
            #if currchar s[r] has a hashed value of more than one
            while charHash[s[r]] > 1:
                charHash[s[l]] -= 1
                l += 1
            maxLen = max(maxLen, r - l + 1)
        return maxLen
            
