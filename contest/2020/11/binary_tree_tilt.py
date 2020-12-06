# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def findTilt(node: TreeNode) -> int:
            if not node:
                return 0
            left = findTilt(node.left)
            right = findTilt(node.right)
            sum = node.val + left + right
            node.val = abs(left - right)
            return sum
        def getSum(node: TreeNode) -> int:
            if not node:
                return 0
            left = getSum(node.left)
            right = getSum(node.right)
            return left + right + node.val
        if not root:
            return 0
        findTilt(root)
        return getSum(root)
