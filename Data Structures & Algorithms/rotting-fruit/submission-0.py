from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -=1
            minutes += 1

        if fresh > 0:
            return -1
        return minutes
