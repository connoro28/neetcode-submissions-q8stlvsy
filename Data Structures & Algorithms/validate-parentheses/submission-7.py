class Solution:
    def isValid(self, s: str) -> bool:
        validMap = {"}":"{", ")":"(","]":"["}
        stack = []
        for c in s:
            if c in validMap:
                if not stack or validMap[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return (len(stack) == 0)
