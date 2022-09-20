# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #check if head itself has this value
        if head:
            while head.val == val and head.next:
                head = head.next
        else:
            return head

        #check for all other elements but not new head
        current = head
        while current:
            #if found delete that node
            if current.next and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        #check for new head before retuting it
        if head.val != val:
            while head:
                print(head.val , end=', ')
                head = head.next
                
        else:
            return None

ll = ListNode(1,ListNode(2,ListNode(6,ListNode(3,ListNode(4,ListNode(5,ListNode(6,None)))))))
t = Solution()
print(t.removeElements(ll, 6))