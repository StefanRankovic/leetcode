# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, node: TreeNode, minval = float('-inf'), maxval = float('inf')):
        if not node:
            return True
        if node.val <= minval or node.val >= maxval:
            return False
        if not self.check(node.left, minval, node.val):
            return False
        return self.check(node.right, node.val, maxval)
        
            
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root)
