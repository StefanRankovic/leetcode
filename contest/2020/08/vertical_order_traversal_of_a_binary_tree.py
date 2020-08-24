# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def place(node, x, y, field):
            if node == None:
                return
            if field[x + 1000][y] is None:
                field[x + 1000][y] = []
            field[x + 1000][y].append(node.val)
            place(node.left, x - 1, y + 1, field)
            place(node.right, x + 1, y + 1, field)
        field = [[None] * 1000 for _ in range(2000)]
        place(root, 0, 0, field)
        res = []
        for i in range(2000):
            row = []
            for j in range(1000):
                if field[i][j] is not None:
                    print(i, j, field[i][j])
                    row.extend(sorted(field[i][j]))
            if len(row) > 0:
                res.append(row)
        return res
