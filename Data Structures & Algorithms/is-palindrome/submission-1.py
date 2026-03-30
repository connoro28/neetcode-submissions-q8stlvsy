class Solution:
    def isPalindrome(self, s: str) -> bool:
        one = ""
        two = ""
        length = len(s)
        for i in range(length):
            popped = s[-1].lower()
            s = s[:-1]
            if popped != " " and popped.isalnum():
                one = popped + one
                two = two + popped
        if one == two:
            return True
        else:
            return False
