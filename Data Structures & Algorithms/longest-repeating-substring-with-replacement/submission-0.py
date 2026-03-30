class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        l = 0
        maxFreq = 0
        maxLength = 0
        for r in range(len(s)):
            currLen = r - l + 1
            charMap[s[r]] = charMap.get(s[r], 0) + 1
            for i in charMap:
                freq = charMap[i]
                maxFreq = max(freq, maxFreq)
            while currLen - maxFreq > k:
                charMap[s[l]] -= 1
                l += 1
                maxFreq = 0
                for i in charMap:
                    freq = charMap[i]
                    maxFreq = max(freq, maxFreq)
                currLen = r - l + 1
            maxLength = max(maxLength, currLen)
        return maxLength
                
            
            
            
        
        