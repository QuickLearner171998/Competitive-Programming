"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 
        start = head
        not_assigned = None
        while head:
            temp = head.next
            new_node= Node(head.val)
            if not_assigned:
                not_assigned.next = new_node
            not_assigned = new_node
            head.next = new_node
            new_node.random = head
            head = temp
            
            
        not_assigned.next = None
        ans = start.next
        t=ans
        while t:
            
            if t.random.random:
                t.random = t.random.random.next
            else:
                t.random = None
            
            t=t.next
            
        return ans
        