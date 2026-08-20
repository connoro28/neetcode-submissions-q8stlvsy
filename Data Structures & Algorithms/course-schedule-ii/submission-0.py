from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        grid = defaultdict(list)
        for course, prereq in prerequisites:
            grid[course].append(prereq)
        
        visiting = set()
        topSort = []
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in grid[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            topSort.append(node)
            visited.add(node)
            return True
        
        for n in range(numCourses):
            if n not in visited:
                if not dfs(n):
                    return []
        return topSort

            