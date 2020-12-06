# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = head
        head = head.next
        while cur and cur.next:
            second = cur.next
            third = cur.next.next
            second.next = cur
            cur.next = third
            if third and third.next:
                cur.next = third.next
            cur = third
        return head
        
