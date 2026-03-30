class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""
        for part in path.split("/"):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)
            

