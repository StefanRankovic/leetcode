class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ships = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    top = board[i-1][j] != 'X' if i > 0 else True
                    left = board[i][j-1] != 'X' if j > 0 else True
                    if top and left:
                        ships += 1
        return ships
