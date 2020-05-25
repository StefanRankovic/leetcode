class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = self.generate(numRows - 1)
        current = []
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                current.append(1)
            else:
                current.append(result[-1][i-1] + result[-1][i])
        result.append(current)
        return result
