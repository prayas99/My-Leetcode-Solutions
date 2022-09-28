# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        root = head
        while root:
            if n == k - 1:
                tar = root
            root = root.next
            n += 1 
        idx = 0
        root = head
        while root:            
            idx += 1
            if idx == n - k + 1:
                root.val, tar.val = tar.val, root.val
                break
            root = root.next
        return head