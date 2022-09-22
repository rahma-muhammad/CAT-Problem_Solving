# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            if not temp:
                break
            prev = curr
            curr = temp
            
        #Just to print it   
        while curr:
            print(curr.val , end=', ')
            curr = curr.next
            
ll = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7, None)))))))
t = Solution()
t.reverseList(ll)