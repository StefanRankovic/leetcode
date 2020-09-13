from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def state(i, j):
            if board[i][j] == 0 or board[i][j] == 2:
                return 0
            else:
                return 1
        def around(i, j):
            live = 0
            if i > 0:
                if j > 0:
                    live += state(i-1, j-1)
                live += state(i-1, j)
                if j < len(board[0])-1:
                    live += state(i-1, j+1)
            if i < len(board)-1:
                if j > 0:
                    live += state(i+1, j-1)
                live += state(i+1, j)
                if j < len(board[0])-1:
                    live += state(i+1, j+1)
            if j > 0:
                live += state(i, j-1)
            if j < len(board[0])-1:
                live += state(i, j+1)
            return live
        for i in range(len(board)):
            for j in range(len(board[0])):
                live = around(i, j)
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and not 2 <= live <= 3:
                    board[i][j] = 3
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

