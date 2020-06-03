# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode()
        carry = 0
        while l1 is not None or l2 is not None:
            first = 0
            second = 0
            if l1 is not None:
                first = l1.val
                l1 = l1.next
            if l2 is not None:
                second = l2.val
                l2 = l2.next
            total = first + second + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit, None)
            current = current.next
        if carry > 0:
            current.next = ListNode(carry, None)
        return head.next
            
