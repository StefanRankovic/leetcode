# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def checkNode(self, node: ListNode):
        if not node:
            return True
        result = self.checkNode(node.next)
        if not result:
            return result
        result = self.counterpart.val == node.val
        self.counterpart = self.counterpart.next
        return result 
    
    def isPalindrome(self, head: ListNode) -> bool:
        self.counterpart = head
        return self.checkNode(head)
