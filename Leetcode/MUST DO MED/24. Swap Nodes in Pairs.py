# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None:
            return 
        start = head
        if head and head.next:
            start = head.next
            head.next = start.next
            start.next = head
            prev = head
            head = head.next
            
        while head:
            if head.next:
                curr = head
                nxt = head.next
                prev.next = nxt
                head = nxt.next
                nxt.next = curr
                prev = curr
                curr.next = head
            else:
                head = head.next
        return start