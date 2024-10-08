from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        current = dummyHead
        carry = 0
        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next
            l2 = l2.next
        while l1 and carry:
            carry, digit = divmod(l1.val + carry, 10)
            current.next = ListNode(digit)
            current = current.next
            l1 = l1.next
        while l2 and carry:
            carry, digit = divmod(l2.val + carry, 10)
            current.next = ListNode(digit)
            current = current.next
            l2 = l2.next
        if l1:
            current.next = l1
        elif l2:
            current.next = l2
        elif carry:
            current.next = ListNode(1)
        return dummyHead.next
