# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        seen = [0] * 10
        def dfs(node):
            cnt = 0
            seen[node.val] += 1
            if not node.left and not node.right:
                odds = len([s for s in seen if s % 2 == 1])
                if odds < 2:
                    cnt = 1
            if node.left:
                cnt += dfs(node.left)
            if node.right:
                cnt += dfs(node.right)
            seen[node.val] -= 1
            return cnt
        return dfs(root)
