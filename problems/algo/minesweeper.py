from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def in_bounds(i, j): 
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        def is_mine(i, j):
            return board[i][j] if in_bounds(i,j) else 'E'
        def step(i, j):
            if not in_bounds(i,j) or board[i][j] != 'E':
                return
            mines = [is_mine(i+1, j+1), 
                     is_mine(i+1, j),
                     is_mine(i+1, j-1),
                     is_mine(i, j+1),
                     is_mine(i, j-1),
                     is_mine(i-1, j+1),
                     is_mine(i-1, j),
                     is_mine(i-1, j-1),
                    ].count('M')
            if mines > 0:
                board[i][j] = str(mines)
            else:
                board[i][j] = 'B'
                step(i+1, j+1), 
                step(i+1, j)
                step(i+1, j-1)
                step(i, j+1)
                step(i, j-1)
                step(i-1, j+1)
                step(i-1, j)
                step(i-1, j-1)
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            step(click[0], click[1])
        return board
