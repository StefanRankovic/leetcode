from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        checked = [list([False for _ in range(len(board[0]))]) for _ in range(len(board))]
        def trace(i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if checked[i][j]:
                return False
            if board[i][j] == word[k]:
                if len(word) == k + 1:
                    return True
                checked[i][j] = True
                if trace(i + 1, j, k+1):
                    return True
                if trace(i - 1, j, k+1):
                    return True
                if trace(i, j-1, k+1):
                    return True
                if trace(i, j+1, k+1):
                    return True
                checked[i][j] = False
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if trace(i, j, 0):
                    return True
        return False
                    
