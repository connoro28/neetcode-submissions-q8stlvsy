class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(i,r,c):
            if (i == len(word)-1) and board[r][c] == word[i]:
                return True
            if board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            for dr, dc in [(1,0),(-1,0),(0,-1),(0,1)]:
                nr, nc = dr + r, dc + c
                if 0 <= nr < rows and 0 <= nc < cols:
                    if dfs(i+1, nr, nc):
                        return True
            board[r][c] = word[i]
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(0, r, c):
                        return True
        return False
            


