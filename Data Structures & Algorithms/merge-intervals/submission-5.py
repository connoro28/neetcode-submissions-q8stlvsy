class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for i in range(len(intervals)):
            if stack:
                if intervals[i][0] <= stack[-1][-1]:
                    stack[-1] = [min(intervals[i][0], stack[-1][0]), max(intervals[i][-1], stack[-1][-1])]
                else:
                    stack.append(intervals[i])
            else:
                stack.append(intervals[i])
        return stack