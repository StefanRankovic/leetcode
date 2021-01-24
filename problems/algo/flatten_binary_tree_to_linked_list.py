# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        if root.left:
            root.left, root.right = root.right, root.left
        if root.left:
            rightmost = root.right
            while rightmost.right:
                rightmost = rightmost.right
            rightmost.right = root.left
            root.left = None
        return self.flatten(root.right)
