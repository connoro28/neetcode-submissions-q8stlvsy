class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x,y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[rx] = ry
            return True
        for x,y in edges:
            if not union(x,y):
                return [x,y]
        return []
