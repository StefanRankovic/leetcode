class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def next_sibling(child, parent):
            cur = parent.next
            while cur:
                if cur.left:
                    child.next = cur.left
                    break
                elif cur.right:
                    child.next = cur.right
                    break
                else:
                    cur = cur.next
        def connect(node):
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    next_sibling(node.left, node)
            if node.right:
                next_sibling(node.right, node)
            if node.right:
                connect(node.right)
            if node.left: 
                connect(node.left)
        if root:
            connect(root)
        return root
