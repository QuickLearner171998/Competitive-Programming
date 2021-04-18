# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getL(head):
            l = 0
            while head:
                head=head.next
                l+=1
            return l
        l1 = getL(headA)
        l2 = getL(headB)
        diff = l1-l2
        for i in range(diff):
            headA = headA.next
        for j in range((-1*diff)):
            headB =  headB.next
        
        while headA and headB:
            if headA==None and not headB:
                return 
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next