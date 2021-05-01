# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head : return
        if not head.next: return
        if not head.next.next: return
        p = head.next.next
        q = head.next

        while q and p:
            if p.next:
                p=p.next.next
                q=q.next
            else:
                return 
            if p==q:
                p = head
                print(q.val)
                while p != q:
                    p = p.next
                    q = q.next
                return p
