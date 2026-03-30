class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""
        for p in path.split("/"):
            if p == "." or p == "":
                continue
            if p == ".." and stack:
                stack.pop()
            elif p == "..":
                continue
            else:
                stack.append(p)
        res = "/" + "/".join(stack)
        return res
