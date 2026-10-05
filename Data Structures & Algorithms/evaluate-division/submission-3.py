class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjacencyMap = defaultdict(list)
        for eq, value in zip(equations, values):
            a, b = eq
            adjacencyMap[a].append((b, value))
            adjacencyMap[b].append((a, 1/value))
        
        def dfs(source, target, visited):
            if source not in adjacencyMap or target not in adjacencyMap:
                return -1
            if source == target:
                return 1
            
            visited.add(source)
            for nei, weight in adjacencyMap[source]:
                if nei not in visited:
                    result = dfs(nei, target, visited)
                    if result != -1:
                        return result * weight
            return -1
        
        res = []
        for q in queries:
            a, b = q
            res.append(dfs(a, b, set()))
        return res

            