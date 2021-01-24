# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == None or original == target:
            return cloned
        lnode = self.getTargetCopy(original.left, cloned.left, target)
        if lnode is not None:
            return lnode
        rnode = self.getTargetCopy(original.right, cloned.right, target)
        return rnode
