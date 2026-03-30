class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        count = 0

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        while l < r:
            if s[l] != s[r]:
                return (isPalindrome(l+1, r) or isPalindrome(l,r-1))
            else:
                l+=1
                r-=1
        return True
