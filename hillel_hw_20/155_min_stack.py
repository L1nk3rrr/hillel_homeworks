# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# Implement the MinStack class:
#
# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1],val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(3)
    assert (s.getMin() == -3)
    s.pop()
    assert (s.top() == 0)
    assert (s.getMin() == -2)
