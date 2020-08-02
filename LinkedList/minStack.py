"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks."""


class Node:
    def __init__(self, val=None, mini=None, next=None):
        self.val = val
        self.min = mini
        self.next = next


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.mini = float('inf')

    def push(self, x: int) -> None:
        if self.mini == float('inf'):
            newNode = Node(x)
        else:
            newNode = Node(x, self.mini, self.head)
        self.head = newNode
        self.mini = min(self.mini, x) if self.mini != None else x

    def pop(self) -> None:
        if self.head:
            self.mini = self.head.min
            self.head = self.head.next

    def top(self) -> int:
        return self.head.val if self.head else 0

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
