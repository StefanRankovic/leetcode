# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                data.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                data.append(None)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = [TreeNode(x) if x is not None else None for x in data]
        root = nodes.pop(0)
        queue = [root]
        while len(nodes) > 0:
            cur = queue.pop(0)
            if cur:
                cur.left = nodes.pop(0)
                cur.right = nodes.pop(0)
                queue.append(cur.left)
                queue.append(cur.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
