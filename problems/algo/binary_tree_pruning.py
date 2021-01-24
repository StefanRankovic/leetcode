# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def postorder(node):
            if not node:
                return False
            l = postorder(node.left)
            if not l:
                node.left = None
            r = postorder(node.right)
            if not r:
                node.right = None
            return node.val == 1 or l or r
        if not postorder(root):
            root = None
        return root
                
