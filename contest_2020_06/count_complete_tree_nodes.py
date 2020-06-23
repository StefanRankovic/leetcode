# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.num = 0
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return self.num
        self.num += 1
        self.countNodes(root.left)
        self.countNodes(root.right)
        return self.num
