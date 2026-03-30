class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in parenMap:
                if not stack or stack[-1] != parenMap[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
