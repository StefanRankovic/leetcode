# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        size = 1
        tail = head
        while tail.next:
            size += 1
            tail = tail.next
        k = size - (k % size)
        if k == 0:
            return head
        tail.next = head
        while k > 0:
            k -= 1
            tail = tail.next
        head = tail.next
        tail.next = None
        return head
