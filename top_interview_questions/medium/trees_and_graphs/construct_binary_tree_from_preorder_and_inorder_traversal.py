# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildSubtree(preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            cur = preorder[0]
            ind = inorder.index(cur)
            l_in = inorder[:ind]
            r_in = inorder[ind+1:]
            l_pr = preorder[1:ind+1]
            r_pr = preorder[ind+1:]
            node = TreeNode(val=cur)
            node.left = buildSubtree(l_pr, l_in)
            node.right = buildSubtree(r_pr, r_in)
            return node
        return buildSubtree(preorder, inorder)
