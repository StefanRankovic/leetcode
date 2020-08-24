# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, current, node):
        current = current * 10 + node.val
        if node.left is None and node.right is None:
            self.total += current
            return
        if node.left is not None:
            self.visit(current, node.left)
        if node.right is not None:
            self.visit(current, node.right)
    
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.total = 0
        self.visit(0, root)
        return self.total
