"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        # def pre(root, ans):
        #     if not root:
        #         return
        #     ans.append(root.val)
        #     for child in root.children:
        #         pre(child, ans)
        # pre(root, ans)
        # return ans
        stk = root and [root] # none and [] = none, 1 and [1] = [1]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            for i in range(len(node.children)-1, -1, -1):
                if node.children[i]:
                    stk.append(node.children[i])
        return ans