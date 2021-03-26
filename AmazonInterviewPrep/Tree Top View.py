"""
Tree : Top View

"""
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def topView(root):
    #Write your code here
    q = [(root, 0)]
    d = {}
    # ndLevel = 0
    while(len(q)):
        
        
        for i in range(len(q)):
            nd, l = q.pop(0)
            if l not in d:
                d[l] = nd.info
            if nd.left:
                q.append((nd.left, l-1))
                
            if nd.right:
                q.append((nd.right, l+1))
                
    for i in sorted(d):
        print(d[i], end = " ")
    # print('\n')    

