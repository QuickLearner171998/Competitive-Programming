# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        if p:
            q = head.next
        
        while p and q:
            if p==q:
                return True
            p = p.next
            q = q.next
            if q:
                q = q.next
        return False