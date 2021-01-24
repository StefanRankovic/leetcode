# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node, i):
            h1 = height(node.left, i+1) if node.left else i
            h2 = height(node.right, i+1) if node.right else i
            if abs(h1-h2) > 1:
                raise ValueError
            return max(h1, h2)
        if not root:
            return True
        try:
            height(root, 0)
            return True
        except ValueError:
            return False
