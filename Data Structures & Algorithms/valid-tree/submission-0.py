from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphs = defaultdict(list)
        for i, j in edges:
            graphs[i].append(j)
            graphs[j].append(i)
        visited = set()
        def dfs(node, parent):
            visited.add(node)
            for nei in graphs[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                if not dfs(nei, node):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return n == len(visited)

