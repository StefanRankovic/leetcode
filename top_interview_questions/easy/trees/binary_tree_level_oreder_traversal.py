# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.order = []
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def helper(node, level):
            if not node:
                return
            if len(self.order) <= level:
                self.order.append([])
            self.order[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        return self.order
            
