# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def delete(node):
            if not node.left and not node.right:
                return None
            elif not node.left and node.right:
                return node.right
            elif node.left and not node.right:
                return node.left
            else:
                left = node.right
                while left.left:
                    left = left.left
                left.left = node.left
                return node.right
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root = delete(root)
        return root
            
