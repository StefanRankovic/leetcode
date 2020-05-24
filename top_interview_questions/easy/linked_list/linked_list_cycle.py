# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ptr1 = head
        ptr2 = head
        while ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if not ptr2:
                return False
            ptr2 = ptr2.next
            if ptr1 == ptr2:
                return True
        return False
