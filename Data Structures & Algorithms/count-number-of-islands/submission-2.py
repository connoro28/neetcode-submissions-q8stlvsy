class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited = set()
        islands = 0
        row = len(grid)
        col = len(grid[0])

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            visited.add((r,c))
            while queue:
                r, c = queue.popleft()
                directions = [[1,0], [0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    if ((r+dr) in range(row) and
                        (c+dc) in range(col) and
                        (r+dr, c+dc) not in visited and 
                        grid[r+dr][c+dc] == "1"):
                        queue.append((r+dr,c+dc))
                        visited.add((r+dr,c+dc))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands