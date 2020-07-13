# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        def add(node, level, table):
            if node is None:
                return table
            if len(table) < level:
                table.insert(0, [])
            table[-level].append(node.val)
            add(node.left, level + 1, table)
            add(node.right, level + 1, table)
            return table
        return add(root, 1, [])
