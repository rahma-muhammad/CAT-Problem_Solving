# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        size , curr = -1, head
        while curr:
            size += 1
            curr = curr.next
        res = 0
        while head:
            res +=(head.val * (2**size))
            size -= 1
            head = head.next
        return res

ll = ListNode(1,ListNode(0,ListNode(1,None)))
t = Solution()
print(t.getDecimalValue(ll))