# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        running = 0
        if not root:
            return running
        if root.left and not (root.left.left or root.left.right):
            running += root.left.val
        running += self.sumOfLeftLeaves(root.left)
        running += self.sumOfLeftLeaves(root.right)
        return running
