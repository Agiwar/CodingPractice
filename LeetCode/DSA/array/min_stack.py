class MinStack:
    """
    Implement a stack that has method getMin has O(1) time complexity,
        so it's not allowed to go through the entire stack to find out the minium value.
    
    The main idea behind the code is, implement 2 stack which are stack and min_stack,
        stack holds the normal stack property, cuz push, pop, and top is already O(1) time
        but min_stack is the key which this min_stack just stores the current pushed number's value
        is equal or less than the min_stack last number value (the append min value last time),
        we don't need to store each pushed number,
        and then compare the current one and min_stack's last one either
        just tracking the current pushed value is what we want.
    
    Note that when pop stack, if this number is equal to min stack last number,
        min stack does pop as well, which means stack pop the minium value from stack
        so the number of minium in stack has been extracted by 1
    
    time = O(1) for all methods
    space = O(n) for two stack created
    """
    
    def __init__(self):
        self.stack = []
        self._min_stack = []        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self._min_stack[-1]:
            self._min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]




def test_MinStack():
    # LeetCode example
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

    # Edge cases (write your own)
    minStack2 = MinStack()
    minStack2.push(10)
    minStack2.push(-5)
    minStack2.push(7)
    assert minStack2.getMin() == -5
    minStack2.pop()
    assert minStack2.top() == -5
    minStack2.push(0)
    minStack2.push(-5)
    assert minStack2.getMin() == -5
    minStack2.pop()
    assert minStack2.getMin() == -5
    assert minStack2.top() == 0
    minStack2.pop()
    assert minStack2.getMin() == -5
    minStack2.pop()
    assert minStack2.getMin() == 10
    assert minStack2.top() == 10

    print("All tests passed")


if __name__ == "__main__":
    test_MinStack()
