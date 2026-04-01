class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        visited = set()
        row, col = len(grid), len(grid[0])
        maxIslands = 0

        def bfs(r, c):
            visited.add((r,c))
            queue = collections.deque()
            queue.append((r,c))
            currTot = 1
            while queue:
                r, c = queue.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for dr, dc in directions:
                    if ((r+dr) in range(row) and
                        (c+dc) in range(col) and 
                        grid[r+dr][c+dc] == 1 and
                        (r+dr, c+dc) not in visited):
                        visited.add((r+dr, c+dc))
                        queue.append((r+dr, c+dc))
                        currTot += 1
            return currTot


        for r in range(row):
            for c in range(col):
                if (r,c) not in visited and grid[r][c] == 1:
                    currVal = bfs(r,c)
                    maxIslands = max(maxIslands, currVal)
        return maxIslands 