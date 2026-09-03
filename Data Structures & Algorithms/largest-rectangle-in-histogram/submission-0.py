class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxRect = 0
        for i, h in enumerate(heights):
            if not stack:
                stack.append([i, h])
            elif h >= stack[-1][1]:
                stack.append([i,h])
            if h < stack[-1][1]:
                while stack and h < stack[-1][1]:
                    currI, currH = stack.pop()
                    maxRect = max(maxRect, currH * (i-currI))
                stack.append([currI, h])
            else:
                stack.append
        finalI = len(heights)
        while stack:
            currI, currH = stack.pop()
            maxRect = max(maxRect, currH * (finalI - currI))
        return maxRect

                

            