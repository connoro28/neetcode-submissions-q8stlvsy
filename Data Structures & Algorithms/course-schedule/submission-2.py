from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visiting = set()
        visited = set()
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            for nei in graph[node]:
                bl = dfs(nei)
                if not bl:
                    return False
            visiting.remove(node)
            visited.add(node)
            return True
        
        for n in range(numCourses):
            if n not in visited:
                if not dfs(n):
                    return False
        return True




