# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head
        
        start = head
        
        while head:
            temp = start
            partition=head.next
            while partition and temp!=partition :
                if temp.val > partition.val:
                    temp.val, partition.val = partition.val, temp.val
                temp=temp.next
            head=head.next
        return start
                
                