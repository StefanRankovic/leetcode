# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lo = lohead = ListNode()
        hi = hihead = ListNode()
        cur = head
        while cur:
            if cur.val < x:
                lo.next = cur
                lo = lo.next
            else:
                hi.next = cur
                hi = hi.next
            cur = cur.next
        hi.next = None
        lo.next = hihead.next
        return lohead.next
            
