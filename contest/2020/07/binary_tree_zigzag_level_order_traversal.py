# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def visit(node, right, level, result):
            if node is None:
                return
            if len(result) < level:
                result.append([])
            if right:
                result[level - 1].append(node.val)
            else:
                result[level - 1].insert(0, node.val)
            visit(node.left, not right, level + 1, result)
            visit(node.right, not right, level + 1, result)
        result = []
        visit(root, True, 1, result)
        return result
