class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        one = 0;
        two = 0;
        if (len(s) == len(t)):
            for sOne, sTwo in zip(s, t):
                curr = ord(sOne);
                curr = curr * curr
                one += curr;
                curr = ord(sTwo);
                curr = curr * curr
                two += curr;
            if (one == two):
                return True
        return False
