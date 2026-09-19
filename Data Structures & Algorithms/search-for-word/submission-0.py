class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(x, y, i):
            if i == len(word):
                return True
            for dx, dy in ((0,1), (0,-1), (1,0), (-1,0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == word[i]:
                    board[nx][ny] = "#"
                    if dfs(nx, ny, i + 1):
                        return True
                    board[nx][ny] = word[i]
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    board[r][c] = "#"
                    if dfs(r,c, 1):
                        return True
                    board[r][c] = word[0]
        return False



