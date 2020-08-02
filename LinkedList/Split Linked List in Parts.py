"""Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is []."""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        ans = []
        l = 0
        temp = root
        while(temp):
            temp = temp.next
            l += 1
        if k >= l:
            rem = k - l
            temp = root
            while(temp):
                new = ListNode(temp.val)
                ans.append(new)
                temp = temp.next
            while(rem):
                ans.append(None)
                rem -= 1
            return ans
        rem = l % k
        ptr = root
        while(ptr):
            ans.append(ptr)
            stride = l // k
            if rem:
                stride = stride + 1
                rem -= 1
            for i in range(stride - 1):
                ptr = ptr.next
            temp = ptr.next
            ptr.next = None
            ptr = temp
        return ans
