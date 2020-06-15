# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return self.inorder
        self.inorderTraversal(root.left)
        self.inorder.append(root.val)
        self.inorderTraversal(root.right)
        return self.inorder
        
