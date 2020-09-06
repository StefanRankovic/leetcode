# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def visit(node, cnt):
            if not node:
                return (cnt, None)
            cnt, val = visit(node.left, cnt)
            if val is not None:
                return (cnt, val)
            cnt += 1
            if cnt == k:
                return (cnt, node.val)
            cnt, val = visit(node.right, cnt)
            if val is not None:
                return (cnt, val)
            if cnt == k:
                return (cnt, node.val)
            return (cnt, None)
        return visit(root, 0)[1]
