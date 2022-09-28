# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = d = head
        while True:
            for _ in range(n):
                head = head.next
            if not head:
                c = c.next
                break                
            if not head.next:
                d.next = d.next.next
                break
            head = d.next
            d = d.next
        return c