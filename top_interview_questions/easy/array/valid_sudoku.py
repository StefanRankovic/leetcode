class Solution:
    def createCheck(self):
        return dict([(str(i), False) for i in range(1, 10)])
    
    def checkRow(self, board, row):
        check = self.createCheck()
        for i in range(9):
            element = board[row][i]
            if element == '.':
                continue
            if check[element]:
                return False
            check[element] = True
        return True

    def checkColumn(self, board, column):
        check = self.createCheck()
        for i in range(9):
            element = board[i][column]
            if element == '.':
                continue
            if check[element]:
                return False
            check[element] = True
        return True
            
    def checkSquare(self, board, square):
        row = 3 * (square // 3)
        col = 3 * (square % 3)
        check = self.createCheck()
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                element = board[i][j]
                if element == '.':
                    continue
                if check[element]:
                    return False
                check[element] = True
        return True
        
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            valid = self.checkRow(board, row)
            if not valid:
                return False
        for column in range(9):
            valid = self.checkColumn(board, column)
            if not valid:
                return False
        for square in range(9):
            valid = self.checkSquare(board, square)
            if not valid:
                return False
        return True
        
            
