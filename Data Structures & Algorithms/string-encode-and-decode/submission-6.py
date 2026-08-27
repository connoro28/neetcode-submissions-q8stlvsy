class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        curr = ""
        res = []
        while i < len(s):
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j + 1
            for _ in range(length):
                curr+=s[i]
                i+=1
            j = i
            res.append(curr)
            curr = ""
        return res
        
