# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        current = head
        while current :
            length += 1
            current = current.next
        if length % 2 == 0:
            mid = length / 2 + 1
        else:
            mid = (length + 1) / 2
            
        while mid > 1:
            head = head.next
            mid -= 1
            
            
        while head:
            print(head.val , end=', ')
            head = head.next
            
ll = ListNode(1,ListNode(2,ListNode(6,ListNode(3,ListNode(4,ListNode(5,ListNode(6, None)))))))
t = Solution()
t.middleNode(ll)