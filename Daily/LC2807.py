from math import gcd
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current.next:
            insertVal = gcd(current.val, current.next.val)
            current.next = ListNode(val=insertVal, next=current.next)
            current = current.next.next
        return head
