class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for i in strs:
            length = len(i)
            encodedStr += str(length)+"#"+i
        return encodedStr

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            index = s.find("#")
            lengthString = int(s[:index])
            s=s[index+1:]
            res.append(s[:lengthString])
            s=s[lengthString:]
        return res

