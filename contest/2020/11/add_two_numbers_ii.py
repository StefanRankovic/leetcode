# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = number2 = 0
        while l1:
            number1 = number1 * 10 + l1.val
            l1 = l1.next
        while l2:
            number2 = number2 * 10 + l2.val
            l2 = l2.next
        number = number1 + number2
        l3 = None
        while number > 9:
            node = ListNode(number % 10)
            node.next = l3
            l3 = node
            number //= 10
        l3 = ListNode(number, l3)
        return l3
