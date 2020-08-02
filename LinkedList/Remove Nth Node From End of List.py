"""Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        fcnt = 0
        bcnt = 0
        f = b = head
        while(f.next):
            if fcnt - bcnt == n:
                bcnt += 1
                b = b.next

            fcnt += 1
            f = f.next
        if fcnt == n - 1:
            head = b.next
            return head
        b.next = b.next.next
        return head
