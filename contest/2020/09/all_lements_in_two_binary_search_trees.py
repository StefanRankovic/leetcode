# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def traverse(node, storage):
            if not node:
                return
            storage.append(node.val)
            traverse(node.left, storage)
            traverse(node.right, storage)
        storage = []
        traverse(root1, storage)
        traverse(root2, storage)
        storage.sort()
        return storage
