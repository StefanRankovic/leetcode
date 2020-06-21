class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def fill(old, new, i, j, board):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] == old:
                board[i][j] = new
                fill(old, new, i-1, j, board)
                fill(old, new, i+1, j, board)
                fill(old, new, i, j-1, board)
                fill(old, new, i, j+1, board)
                
        if len(board) == 0:
            return
        for i in range(len(board)):
            fill('O', 'T', i, 0, board)
            fill('O', 'T', i, len(board[0])-1, board)
        for i in range(len(board[0])):
            fill('O', 'T', 0, i, board)
            fill('O', 'T', len(board)-1, i, board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                fill('O', 'X', i, j, board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                fill('T', 'O', i, j, board)
        
