from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)
            for nei in graph.get(node, []):
                if nei not in visited:
                    dfs(nei)
        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node)
        return count