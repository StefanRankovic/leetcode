# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def calc(node, acc):
            acc <<= 1
            acc += node.val
            if not node.left and not node.right:
                return acc
            lsum = calc(node.left, acc) if node.left else 0
            rsum = calc(node.right, acc) if node.right else 0
            return lsum + rsum
        return calc(root, 0)
