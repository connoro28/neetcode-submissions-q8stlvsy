from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific  = set()
        atlantic = set()
        pq = deque()
        aq = deque()
        rows = len(heights)
        cols = len(heights[0])
        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    pacific.add((r,c))
                    pq.append((r,c))
                if r == ((rows) - 1) or c == (cols -1):
                    atlantic.add((r,c))
                    aq.append((r,c))
        
        def bfs(q, seen):
            while q:
                r, c = q.popleft()
                curr = heights[r][c]
                for dr, dc in [(1,0), (-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in seen:
                        if heights[nr][nc] >= curr:
                            q.append((nr,nc))
                            seen.add((nr,nc))
        bfs(pq, pacific)
        bfs(aq, atlantic)
        return [[r,c] for r,c in pacific & atlantic]

        
              


