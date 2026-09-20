class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            for dr, dc in [(1,0),(-1,0),(0,-1),(0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[i]:
                    board[nr][nc] = "#"
                    if dfs(nr, nc, i+1):
                        return True
                    board[nr][nc] = word[i]
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    board[r][c] = "#"
                    if dfs(r, c, 1):
                        return True
                    board[r][c] = word[0]
        return False