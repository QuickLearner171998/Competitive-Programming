"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q =[]
        q.append(root)
        l = 0
        ans=[]
        while q:
            nodes_in_q = len(q)
            # print("Nodes in level ", l, nodes_in_q)
            l+=1
            temp=[]
            for _ in range(nodes_in_q):
                proot = q.pop(0)
                temp.append(proot)
                if proot.left:
                    q.append(proot.left)
                if proot.right:
                    q.append(proot.right)
                    
            for i in range(len(temp)):
                if i < len(temp)-1:
                    temp[i].next = temp[i+1]
                else:
                    temp[i].next = None
            ans.append(temp)
            
        return root